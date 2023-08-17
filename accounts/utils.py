
#get user role and redirect spasific page
def detect_user(user):
    if user.role == 1:
        redirecturl = 'vendorDashboard'
        return redirecturl
    if user.role == 2:
           redirecturl = 'customerDashboard'
           return redirecturl
    if user.role == 'none' and user.role == 'is_superadmin':
            redirecturl = '/admin'
            return redirecturl
