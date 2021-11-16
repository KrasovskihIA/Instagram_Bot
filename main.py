from instapy import InstaPy
from instapy.time_util import randomize_time


#Данные для входа
insta_username = 'username'
insta_password = 'passuser'


session = InstaPy(username=insta_username, password=insta_password)
session.login()

#настройки/ Филтр по понимальному количеству подписчиков, игнорирование бизнес аккаунтов, настройки сна, фильтр минимальных лайков
session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, min_followers= 50, min_posts=10)
session.set_skip_users(skip_private=True, skip_no_profile_pic=True, skip_business=True, business_percentage=100)
session.set_action_delays(enabled=True, like=3, comment=5, follow=4, unfollow=5, story=10)
session.set_delimit_liking(enabled=True, max_likes=None, min_likes=10)


#Ставим лайки по тегам и взаимодействуем с пользователем
session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
session.like_by_tags(["ресницытольятти", "наращиваниересництольятти", ",бровитольятти", "Тольятти"], amount=10, interact=True)
#Ставим лайки по местоположению из поста
session.like_by_locations(['224955142/togliatti-russia/'], amount=20)


#Подписываемся на пользователей, поставивших лайки на фото других пользователей
session.follow_likers(['user_1'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
#Подписываемся по местоположению
session.follow_by_locations(['224955142/togliatti-russia/'], amount=50)

session.end()
