from .models import StudyMaster
from .models import FormMaster
from .models import CodeListMaster
from .models import CodeListCodeName
from .models import SdvStatusForAllStudy
from .models import ReasonForChange

from django.contrib import admin

admin.site.register(StudyMaster)
admin.site.register(FormMaster)
admin.site.register(CodeListMaster)
admin.site.register(CodeListCodeName)
admin.site.register(SdvStatusForAllStudy)
admin.site.register(ReasonForChange)


# Register your models here.
