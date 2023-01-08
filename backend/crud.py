from sqlalchemy.orm import Session

from . import models

def create_users(db: Session):
    db_user = models.User(user_id=user.user_id, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_images(db: Session):
    db_image = models.User(poster=image.poster, image_name=image.imagename, image_path=image.image_path, title=image.title, poster_comment=image.poster_comment, good_num=image.good_num)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image



