from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# TODO: DB 연결 엔진을 생성하세요 (create_engine)
# Config 클래스에 정의된 DB URI를 사용하여 엔진을 생성합니다.

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

# TODO: 세션(SessionLocal) 객체를 만드세요 (scoped_session)
# 멀티 스레드 환경에서도 안전하게 사용할 수 있도록 scoped_session을 사용합니다.
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# TODO: Base 클래스를 만드세요 (declarative_base)
# 모든 DB 모델 클래스가 상속받을 기본 클래스입니다.
Base = declarative_base()

def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # TODO: 모델을 import 하세요 (예: from . import models)
    # 테이블 생성을 위해 모델 클래스들이 정의된 파일을 불러옵니다.
    from . import models

    # TODO: DB 테이블을 생성하세요 (Base.metadata.create_all)
    # 정의된 모델을 바탕으로 실제 DB에 테이블을 생성합니다.
    Base.metadata.create_all(bind=engine)

    # TODO: 라우트 블루프린트를 등록하세요 (review_routes 불러와서 app.register_blueprint)
    # 별도의 파일에 분리된 라우트(URL 경로) 기능들을 앱에 연결합니다.
    from .routes.review_routes import review_bp
    app.register_blueprint(review_bp)

    # 요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app