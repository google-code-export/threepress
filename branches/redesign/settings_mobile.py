from settings import *
import settings

TEMPLATE_DIRS_BASE = TEMPLATE_DIRS

TEMPLATE_DIRS = (
    '%s/library/templates/mobile/auth' % ROOT_PATH,    
    '%s/library/templates/mobile' % ROOT_PATH,    
)


TEMPLATE_DIRS += TEMPLATE_DIRS_BASE
print TEMPLATE_DIRS

MOBILE = True
