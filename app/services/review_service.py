from app import SessionLocal
from app.models import Review

# 주의: 파일 상단에서 전역 변수로 db = SessionLocal()을 선언하면 
# 서버가 켜져 있는 동안 하나의 세션만 공유하게 되어 에러가 발생할 수 있습니다.
# 가급적 함수 내부에서 세션을 사용하거나, app에서 설정한 scoped_session을 믿고 사용하세요.

def get_all_reviews():
    """모든 리뷰 조회"""
    return SessionLocal.query(Review).all()


def create_review(title, content, rating):
    """리뷰 생성"""
    new_review = Review(title=title, content=content, rating=rating)
    SessionLocal.add(new_review)
    SessionLocal.commit()
    return new_review


def get_review_by_id(review_id):
    """ID로 리뷰 조회"""
    return SessionLocal.query(Review).filter(Review.id == review_id).first()


def update_review(review_id, title, content, rating):
    """리뷰 수정"""
    review_one = get_review_by_id(review_id)
    
    if not review_one:
        return None
    
    review_one.title = title
    review_one.content = content
    review_one.rating = rating
    
    SessionLocal.commit()
    return review_one


def delete_review(review_id):
    """리뷰 삭제"""
    review = get_review_by_id(review_id)
    if review:
        SessionLocal.delete(review)
        SessionLocal.commit()
        return True
    return False