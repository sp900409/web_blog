from src.common.database import Database
import uuid
import datetime


class Post(object):
    """This is Posts class"""

# Usage:
#
# post = Post(blog_id="1234",
#         title="Another post",
#         content="This is some sample content",
#         author="Peng")
#
# post= Post.from_mongo('394e471249514b3fb64b8fd1dd4c6046')
# print(post)
# posts= Post.from_blog('123')
# for post in posts:
# print(post)

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content =  content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

        # post = Post(blog_id="123", title="a title", content="the content", author="Peng")

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls,_id):
        post_data =  Database.find_one(collection='posts', query={'_id':_id})
        return cls(**post_data)

        # return cls(blog_id=post_data['psot_id'],
        #            title=post_data['title'],
        #            content=post_data['content'],
        #            author=post_data['author'],
        #            created_data=post_data['created_data'],
        #            _id=post_data['_id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]

