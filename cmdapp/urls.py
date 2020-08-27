from rest_framework.routers import SimpleRouter
from cmdapp.views import *

router = SimpleRouter()

router.register('emp-api/',EmpOperations)
router.register('adrs-api/',AddressOperations)

urlpatterns = router.urls