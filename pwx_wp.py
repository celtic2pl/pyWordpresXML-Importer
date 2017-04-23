try:
    import wordpress_xmlrpc as wp_rpc
except ImportError:
    wp_rpc = None
    print('Missing wordpress_xmlrpc module')
    print('Please run...')
    print('"pip install python-wordpress-xmlrpc"')
    exit(1)
import wordpress_xmlrpc.methods as wp_methods


class MyWp:
    def __init__(self):
        self.user = None
        self.password = None
        self.url = None
        self.post = wp_rpc.WordPressPost()

    def create_post(self, title, content):
        conn = wp_rpc.Client(self.url, self.user, self.password)
        self.post.title = title
        self.post.content = content
        self.post.post_status = 'publish'
        self.post.id = conn.call(wp_methods.posts.NewPost(self.post))
        return self.post.id


if __name__ == "__main__":
    wp = MyWp()
    wp.user = 'test'
    wp.password = 'test'
    wp.url = "http://wordpress/xmlrpc.php"

    new_title = "Bla bla"
    new_content = "Magic content :)"
    post_id = wp.create_post(new_title, new_content)
    print("Post id:" + post_id)




