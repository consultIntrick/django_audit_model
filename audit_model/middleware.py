REQUEST_USER = None


class AuditUserMiddleware:
    """ This captures the user from the request object and saves it to the global varaible
    which in turn is used in the models to audit every entry in it
    """

    def process_request(self, request):
        global REQUEST_USER
        REQUEST_USER = request.user
