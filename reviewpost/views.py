from django.shortcuts import render,redirect, get_object_or_404    #redirectはURLを遷移させず、redirectはURLを遷移させる。
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from .models import ReviewModel, UserProfile, Message
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages as django_messages
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('list')
    
    def form_invalid(self, form):
        # ログイン失敗時の処理
        return super().form_invalid(form)
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # エラーが発生した場合の処理
            django_messages.error(request, f'ログインページの読み込み中にエラーが発生しました: {str(e)}')
            return render(request, 'login.html', {'form': AuthenticationForm()})
    
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # ログイン処理中にエラーが発生した場合
            django_messages.error(request, f'ログイン処理中にエラーが発生しました: {str(e)}')
            return render(request, 'login.html', {'form': AuthenticationForm()})

class CustomLogoutView(LogoutView):
    pass

@login_required(login_url='/login')
def listview(request):
    try:
        # ソート機能
        sort = request.GET.get('sort', 'newest')
        
        # N+1問題対策
        base_query = ReviewModel.objects.prefetch_related('likes')

        if sort == 'oldest':
            object_list = base_query.order_by('created_at')
        elif sort == 'likes':
            # いいね数でソート（annotateを使用）
            object_list = base_query.annotate(like_count=Count('likes')).order_by('-like_count')
        else:  # newest (デフォルト)
            object_list = base_query.order_by('-created_at')
        
        return render(request,'list.html',{
            'object_list': object_list,
            'current_sort': sort
        })
    except Exception as e:
        # データベースエラーの場合、空のリストを返す
        from django.contrib import messages
        messages.error(request, f'データの読み込み中にエラーが発生しました: {str(e)}')
        return render(request,'list.html',{
            'object_list': [],
            'current_sort': 'newest'
        })

def columnview(request):
    if request.method == 'POST':
            return redirect('login')
    else:
        return render(request,'login.html',{})

def detailview(request,pk):
    object = get_object_or_404(ReviewModel, pk=pk)
    return render(request, 'detail.html',{'object':object})

@login_required(login_url='/login')
def profileview(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=user)
    user_reviews = ReviewModel.objects.filter(author=user).order_by('-id')
    return render(request, 'profile.html', {
        'profile_user': user,
        'profile': profile,
        'user_reviews': user_reviews
    })

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'profile_edit.html'
    fields = ['bio', 'avatar', 'website', 'location', 'birth_date']
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})

@login_required(login_url='/login')
def inboxview(request):
    received_messages = Message.objects.filter(recipient=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    return render(request, 'inbox.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages
    })

@login_required(login_url='/login')
def message_detailview(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    # メッセージの受信者または送信者のみアクセス可能
    if message.recipient != request.user and message.sender != request.user:
        return redirect('inbox')
    
    # 未読の場合、既読にする
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'message_detail.html', {'message': message})

@login_required(login_url='/login')
def send_messageview(request, recipient_username=None):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        
        try:
            recipient = User.objects.get(username=recipient_username)
            Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                content=content
            )
            django_messages.success(request, 'メッセージを送信しました。')
            return redirect('inbox')
        except User.DoesNotExist:
            django_messages.error(request, '指定されたユーザーが見つかりません。')
    
    # GETリクエストの場合
    recipient = None
    if recipient_username:
        try:
            recipient = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            pass
    
    all_users = User.objects.exclude(id=request.user.id)
    return render(request, 'send_message.html', {
        'recipient': recipient,
        'all_users': all_users
    })

@login_required(login_url='/login')
def like_review(request, review_id):
    if request.method == 'POST':
        review = get_object_or_404(ReviewModel, id=review_id)
        
        if request.user in review.likes.all():
            # いいねを削除
            review.likes.remove(request.user)
            liked = False
        else:
            # いいねを追加
            review.likes.add(request.user)
            liked = True
        
        return JsonResponse({
            'liked': liked,
            'total_likes': review.total_likes()
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('author','title','content','project_image')
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)