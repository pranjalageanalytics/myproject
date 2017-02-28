from table import Table
from table.columns import Column

class UserTypeTable(Table): 
    
    ID = Column(field='user.pk', header='ID')
    
    organization = Column(field='organization', header='organization')
    contact_number = Column(field='contact', header='Contact Number')
    website = Column(field='website', header='Website')
    status = Column(field='host_permission', header='Status',attrs = {'class':'status',},sortable=True)
    email = Column(field='user.email', header='email')
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)
#     approve = Column(field='Approve',header='',attrs = {'class':'fa fa-thumbs-o-up','id':'approve','title':'approve','href':'www.google.com'},sortable=False)
#     reject = Column(field='Reject',header='',attrs= {'class':'fa fa-ban','id':'reject',
#                                                    'title':'reject'},sortable=False)



class UserGroupsTable(Table): 
    
    
    
    ID = Column(field='id', header='ID')
    
    name = Column(field='challenge.title', header='Challenge Name')
    status = Column(field='status.status', header='Status',attrs = {'id':'status',},sortable=True)
   
    email = Column(field='user.user.id', header='Host Name')
    catagory = Column(field='category_location.category.category_name', header='Catagory')
    location = Column(field='category_location.location.city', header='Location')

    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)
#     approve = Column(field='Approve',header='',attrs = {'class':'fa fa-thumbs-o-up','id':'approve','title':'approve'},sortable=False)
#     reject = Column(field='Reject',header='',attrs= {'class':'fa fa-ban','id':'reject',
#                                                    'data-toggle':'modal','data-target':'#deleteApartmentLeasein','title':'reject'},sortable=False)
