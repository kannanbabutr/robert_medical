#Study
from .models import StudyMaster
from .models import FormMaster
from .models import CodeListMaster
from .models import CodeListCodeName
from .models import SdvStatusForAllStudy
from .models import ReasonForChange
from .models import CountryMaster
from .models import MasterParameters
from .models import LevelOne
from .models import LevelTwo
from .models import LevelThree
from .models import StudyLock
from .models import TimeZoneMaster
from .models import DemoStudySignoff
from .models import FormChange
from .models import FunctionMaster

from django.contrib import admin

admin.site.register(StudyMaster)
admin.site.register(FormMaster)
admin.site.register(CodeListMaster)
admin.site.register(CodeListCodeName)
admin.site.register(SdvStatusForAllStudy)
admin.site.register(ReasonForChange)
admin.site.register(CountryMaster)
admin.site.register(MasterParameters)
admin.site.register(LevelOne)
admin.site.register(LevelTwo)
admin.site.register(LevelThree)
admin.site.register(StudyLock)
admin.site.register(TimeZoneMaster)
admin.site.register(DemoStudySignoff)
admin.site.register(FormChange)
admin.site.register(FunctionMaster)


# Register your models here.
