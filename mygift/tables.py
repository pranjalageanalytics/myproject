from table import Table
from table.columns import Column
from django.contrib.auth.models import User

class UserTypeTable(Table): 
    Number = Column(header='ID' , attrs={'id':'number'})
    ID = Column(field='user.pk', header='Organization',sortable=True,attrs = {'hidden':True})
    
    organization = Column(field='organization', header='Contact Number')
    contact_number = Column(field='contact', header='Website')
    website = Column(field='website', header='Status')
    status = Column(field='host_permission', header='email',attrs = {'class':'status',},sortable=True)

    email = Column(field='user.email', header='View')
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)
#     approve = Column(field='Approve',header='',attrs = {'class':'fa fa-thumbs-o-up','id':'approve','title':'approve','href':'www.google.com'},sortable=False)
#     reject = Column(field='Reject',header='',attrs= {'class':'fa fa-ban','id':'reject',
#                                                    'title':'reject'},sortable=False)
class UserType1(Table):
    Number = Column(header='ID' , attrs={'id':'number'})
    ID = Column(field='user.pk', header='email',sortable=True,attrs={'hidden':True})
    email = Column(field='user.email', header='Gender')
    gender = Column(field='gender', header='Contact')
    contact_number = Column(field='contact', header='View')
    #date_of_birth = Column(field='date_of_birth', header='View')
    #status = Column(field='host_permission', header='email',attrs = {'class':'status',},sortable=True)
    status = Column(field='host_permission', header='',attrs={'class':'status','hidden':True},sortable=True,visible=False)

    
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)
    
    


class UserGroupsTable(Table): 
    
    
    Number = Column(header='ID' , attrs={'id':'number'})
    ID = Column(field='id', header='Challenge Name',sortable=True,attrs = {'hidden':True} )
    
    name = Column(field='challenge.title', header='Status')
    status = Column(field='status.status', header='Host Name',attrs = {'id':'status',},sortable=True)
   
    email = Column(field='user.user.id',header='View'   )
#     catagory = Column(field='category_location.category.category_name', header='Location')
#     location = Column(field='category_location.location.city', header='')

    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)
#     approve = Column(field='Approve',header='',attrs = {'class':'fa fa-thumbs-o-up','id':'approve','title':'approve'},sortable=False)
#     reject = Column(field='Reject',header='',attrs= {'class':'fa fa-ban','id':'reject',
#                                                    'data-toggle':'modal','data-target':'#deleteApartmentLeasein','title':'reject'},sortable=False)




class notificationTable(Table):
    Number = Column(header='Email' , attrs = {'hidden':True})
    ID = Column(field='pk', header='Time',sortable=True,attrs = {'hidden':True},)
    actor = Column(field='actor', header='View')
    time= Column(field='timesince', header='')
    status= Column(field='unread', header='',attrs={'id':'status'},visible=False)
    
    
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view','data-toggle':'modal','data-target':'#myModal',},sortable=False)    


