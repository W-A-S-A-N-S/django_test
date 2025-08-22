"""
요구사항:
1. /calculator/add/5/3/ → "5 + 3 = 8" 표시
2. /calculator/multiply/4/7/ → "4 × 7 = 28" 표시

작성할 코드:
"""

# views.py
def add(request, num1, num2):
    # 구현하세요
    result = num1 + num2

def multiply(request, num1, num2):
    # 구현하세요
    result = num1 * num2

# urls.py
urlpatterns = [
    # URL 패턴 작성
    path('add/<int:num1>/<int:num2>/', views.add)
    path('multiply/<int:num1>/<int:num2>/', views.multiply)
]
