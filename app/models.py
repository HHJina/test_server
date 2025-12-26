from sqlalchemy import Column, Integer, String, Text, DateTime, func
from . import Base

# TODO: Review 모델 클래스를 만드세요 (Base 상속)
class Review(Base):
    """리뷰 정보를 저장하는 테이블 모델"""
    __tablename__ = "reviews" # 데이터베이스에서 사용할 테이블 이름

    # TODO: id, title, content, rating 컬럼을 정의하세요
    # 고유 식별자 (Primary Key)
    id = Column(Integer, primary_key=True, index=True)
    
    # 제목 (최대 100자, 비어있을 수 없음)
    title = Column(String(100), nullable=False)
    
    # 내용 (긴 텍스트)
    content = Column(Text, nullable=False)
    
    # 별점 (정수형)
    rating = Column(Integer, nullable=False)

    # 생성일
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # 수정일
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())