

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Memo
from .forms import MemoModelForm, ArtModelForm


def base1(request):
    return render(request, 'polls/base.html')

def index(request):

    return render(request=request, template_name="polls/index.html")

# def blog_list(request):
#     return render(request, "not good html")


def hello(request):
    """
    가장 간단한 View 함수
    - request: Django가 자동으로 전달하는 요청 정보
    - HttpResponse: 브라우저에 보낼 응답
    """
    return HttpResponse("안녕하세요")

def lion(request, name):
    return HttpResponse(f"<h1>{name}<h1>")

def good(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🎉 GOOD PAGE 🎉</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow-x: hidden;
            }
            
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            
            .title {
                font-size: 4rem;
                color: #fff;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                animation: rainbow 3s linear infinite;
            }
            
            .subtitle {
                font-size: 1.5rem;
                color: #f0f0f0;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }
            
            .feature-card {
                background: rgba(255, 255, 255, 0.2);
                padding: 25px;
                border-radius: 15px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                cursor: pointer;
            }
            
            .feature-card:hover {
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 15px;
                display: block;
            }
            
            .feature-title {
                color: #fff;
                font-size: 1.2rem;
                font-weight: bold;
                margin-bottom: 10px;
            }
            
            .feature-desc {
                color: #e0e0e0;
                font-size: 0.9rem;
            }
            
            .cta-button {
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                color: white;
                padding: 15px 40px;
                border: none;
                border-radius: 50px;
                font-size: 1.2rem;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 20px;
                text-decoration: none;
                display: inline-block;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            
            .cta-button:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.3);
                filter: brightness(1.1);
            }
            
            .particles {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
            
            .particle {
                position: absolute;
                background: #fff;
                border-radius: 50%;
                opacity: 0.7;
            }
            
            @keyframes floating {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
            
            @keyframes rainbow {
                0% { color: #ff6b6b; }
                16.66% { color: #4ecdc4; }
                33.33% { color: #45b7d1; }
                50% { color: #96ceb4; }
                66.66% { color: #feca57; }
                83.33% { color: #ff9ff3; }
                100% { color: #ff6b6b; }
            }
            
            @keyframes float {
                0%, 100% { 
                    transform: translateY(0px) rotate(0deg); 
                    opacity: 0;
                }
                10%, 90% {
                    opacity: 0.7;
                }
                50% { 
                    transform: translateY(-100px) rotate(180deg); 
                    opacity: 1;
                }
            }
            
            .stats {
                display: flex;
                justify-content: space-around;
                margin: 30px 0;
                flex-wrap: wrap;
            }
            
            .stat-item {
                text-align: center;
                color: #fff;
                margin: 10px;
            }
            
            .stat-number {
                font-size: 2.5rem;
                font-weight: bold;
                display: block;
                color: #4ecdc4;
            }
            
            .stat-label {
                font-size: 0.9rem;
                opacity: 0.8;
            }
            
            @media (max-width: 768px) {
                .container {
                    margin: 20px;
                    padding: 30px;
                }
                
                .title {
                    font-size: 2.5rem;
                }
                
                .features {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="particles">
            <div class="particle" style="left: 10%; animation-delay: 0s; width: 4px; height: 4px;"></div>
            <div class="particle" style="left: 20%; animation-delay: 1s; width: 6px; height: 6px;"></div>
            <div class="particle" style="left: 30%; animation-delay: 2s; width: 4px; height: 4px;"></div>
            <div class="particle" style="left: 40%; animation-delay: 3s; width: 8px; height: 8px;"></div>
            <div class="particle" style="left: 50%; animation-delay: 4s; width: 5px; height: 5px;"></div>
            <div class="particle" style="left: 60%; animation-delay: 5s; width: 7px; height: 7px;"></div>
            <div class="particle" style="left: 70%; animation-delay: 6s; width: 4px; height: 4px;"></div>
            <div class="particle" style="left: 80%; animation-delay: 7s; width: 6px; height: 6px;"></div>
            <div class="particle" style="left: 90%; animation-delay: 8s; width: 5px; height: 5px;"></div>
        </div>
        
        <div class="container">
            <h1 class="title">🌟 GOOD PAGE 🌟</h1>
            <p class="subtitle">Django로 만든 멋진 웹페이지입니다!</p>
            
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Django</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">2025</span>
                    <span class="stat-label">최신 기술</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">∞</span>
                    <span class="stat-label">가능성</span>
                </div>
            </div>
            
            <div class="features">
                <div class="feature-card">
                    <span class="feature-icon">🚀</span>
                    <div class="feature-title">빠른 성능</div>
                    <div class="feature-desc">Django의 강력한 성능으로 빠른 웹 개발</div>
                </div>
                
                <div class="feature-card">
                    <span class="feature-icon">🎨</span>
                    <div class="feature-title">아름다운 디자인</div>
                    <div class="feature-desc">현대적이고 반응형 웹 디자인</div>
                </div>
                
                <div class="feature-card">
                    <span class="feature-icon">⚡</span>
                    <div class="feature-title">동적 효과</div>
                    <div class="feature-desc">CSS 애니메이션과 인터랙티브 요소</div>
                </div>
                
                <div class="feature-card">
                    <span class="feature-icon">📱</span>
                    <div class="feature-title">모바일 친화적</div>
                    <div class="feature-desc">모든 디바이스에서 완벽한 호환성</div>
                </div>
            </div>
            
            <a href="/" class="cta-button">홈으로 돌아가기</a>
            <a href="/hello/" class="cta-button">Hello 페이지</a>
            <a href="/lion/" class="cta-button">Lion 페이지</a>
        </div>
        
        <script>
            // 간단한 인터랙션 추가
            document.querySelectorAll('.feature-card').forEach(card => {
                card.addEventListener('click', function() {
                    this.style.background = 'rgba(255, 255, 255, 0.3)';
                    setTimeout(() => {
                        this.style.background = 'rgba(255, 255, 255, 0.2)';
                    }, 200);
                });
            });
            
            // 추가 파티클 생성
            function createParticle() {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.width = particle.style.height = Math.random() * 8 + 4 + 'px';
                particle.style.animationDelay = Math.random() * 6 + 's';
                document.querySelector('.particles').appendChild(particle);
                
                setTimeout(() => {
                    particle.remove();
                }, 6000);
            }
            
            setInterval(createParticle, 800);
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def moon(request):
    return HttpResponse("<h2>문종현<h2>")

def add(request, num1, num2):
    # 구현하세요
    result = num1 + num2
    return HttpResponse(result)

def multiply(request, num1, num2):
    # 구현하세요
    result = num1 * num2
    return HttpResponse(result)

from .models import Article, Memo


def memo_list(request):
    memos = Memo.objects.all()
    print(f"뷰에서 가져온 메모 개수: {memos.count()}")
    return render(request, 'polls/memo_list.html', {'memos': memos})

#content = "제목 : 타이틀"

def one_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    content = f"""<h1>제목 : {memo.title}</h1>
    내용 : {memo.content}<br>
    중요 : {memo.is_important}<br>
    생성시각 : {memo.created_at}<br>
    """
    return HttpResponse(content)

def memo_create(request):
    """ModelForm을 사용한 메모 작성"""
    if request.method == 'POST':
        form = MemoModelForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)  # 한 줄로 저장 완료!
            memo.author = request.user
            memo.save() 
            return redirect('polls:memo_detail', pk=memo.pk)
    else:
        form = MemoModelForm()

    return render(request, 'polls/memo_form.html', {
        'form': form,
        'title': '메모 작성'
    })

def memo_list(request):
    """메모 목록 보기"""
    memos = Memo.objects.all()  # 자동으로 created_at 역순 정렬됨
    return render(request, 'polls/memo_list.html', {'memos': memos})

def memo_detail(request, pk):
    """메모 상세 보기"""
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'polls/memo_detail.html', {'memo': memo})

def memo_update(request, pk):
    """메모 수정"""
    memo = get_object_or_404(Memo, pk=pk)

    if request.method == 'POST':
        form = MemoModelForm(request.POST, instance=memo)  # instance 전달!
        if form.is_valid():
            form.save()
            return redirect('polls:memo_detail', pk=memo.pk)
    else:
        form = MemoModelForm(instance=memo)  # 기존 데이터로 폼 채우기

    return render(request, 'polls/memo_form.html', {
        'form': form,
        'title': '메모 수정'
    })

def memo_delete(request, pk):
    """메모 삭제"""
    memo = get_object_or_404(Memo, pk=pk)

    if request.method == 'POST':
        memo.delete()
        return redirect('polls:memo_list')

    return render(request, 'polls/memo_confirm_delete.html', {'memo': memo})



def sans(request):
    return render(request, 'polls/sans.html')

def papyrus(request):
    return render(request, 'polls/papyrus.html')

#CRUD
#UPDATE DELETE 해당하는 뷰, 템플릿 구성
#각 템플릿을 base.html 적용 

# def memo_create(request):
#     """ModelForm을 사용한 메모 작성"""
#     if request.method == 'POST':
#         form = MemoModelForm(request.POST)
#         if form.is_valid():
#             memo = form.save()  # 한 줄로 저장 완료!
#             return redirect('polls:memo_detail', pk=memo.pk)
#     else:
#         form = MemoModelForm()

#     return render(request, 'polls/memo_form.html', {
#         'form': form,
#         'title': '메모 작성'
#     })

def art_create(request):
    if request.method == 'POST':
        form = ArtModelForm(request.POST)
        if form.is_valid():
            art = form.save()
            return redirect('polls:art_list', pk=art.pk)
    else:
        form = ArtModelForm()

    return render(request, 'polls/art_form.html', {
        'form': form,
        'title': '게시글 작성'
    })