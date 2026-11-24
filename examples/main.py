from bobtail_admin import BobtailAdmin

class Blogs:

    def get(self, req, res):
        res.set_body({id: 1})

routes = [
    (Blogs(), ["/blogs", "blogs/{blog_id:int}"])
]

if __name__ == "__main__":
    bobtail = BobtailAdmin(routes=routes)
    bobtail.run(port=8000)