import unittest
from manage import Author,db,app


class   TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        app.testing=True
        app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:3306/FlaskTest'
        db.create_all()


    def test_da(self):

        a=Author(name='yeye')

        db.session.add(a)
        db.session.commit()

        result_author=Author.query.filter_by(name='yeye').first()
        print(result_author.name)
        self.assertIsNotNone(result_author)

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()




