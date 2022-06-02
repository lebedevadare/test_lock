from .BasePage import BasePage
from locators import HomePost


class PostPage(BasePage):
    def find_element_post_home(self, index):
        self._get_element(HomePost.post.header_post_home_page, index=index)
        self._get_element(HomePost.post.post_body_at_home, index=index)
        self._get_element(HomePost.post.post_user_at_home, index=index)
