# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
# 
# from django.db import models
# from django.contrib.auth.models import User,Group
# from django.conf import settings
# get_media=settings.MEDIA_ROOT
# from django.utils import timezone
# from django.contrib.auth.models import User
# 
# 
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
# 
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     group = models.ForeignKey(Group, models.DO_NOTHING)
# 
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
# 
# 
# 
# class CategoryLocationRel(models.Model):
#     category = models.ForeignKey('CategoryType', models.DO_NOTHING, db_column='category', blank=True, null=True)
#     location = models.ForeignKey('LocationType', models.DO_NOTHING, db_column='location', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'category_location_rel'
#     
# 
# class CategoryType(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=70)
#     category_image=models.ImageField(blank=True,null=True)
#     class Meta:
#         managed = False
#         db_table = 'category_type'
# 
#     def __str__(self):
#         return str(self.category_name) or u''
# 
# class Category(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=70)
#     category_image=models.CharField(max_length=500,blank=True,null=True)
#     class Meta:
#         managed = False
#         db_table = 'category_type'
# 
#     def __str__(self):
#         return str(self.category_name) or u''    
#     
# class ChallengeCreatorRankingRel(models.Model):
#     rank = models.ForeignKey('RankType', models.DO_NOTHING, db_column='rank', blank=True, null=True)
#     user_challenge_category_location = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'challenge_creator_ranking_rel'
# 
# 
# class ChallengeType(models.Model):
#     challenge_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=70, blank=True, null=True)
#     photo = models.CharField(max_length=500, blank=True, null=True)
#    
#     start_date = models.DateField(blank=True, null=True)
#     post_date = models.DateTimeField(default=timezone.now())
#     end_date = models.DateField(blank=True, null=True)
#     venue = models.CharField(max_length=500, blank=True, null=True)
#     direction = models.CharField(max_length=1000, blank=True, null=True)
#     contact_no = models.CharField(max_length=15, blank=True, null=True)
#     description = models.CharField(max_length=1000, blank=True, null=True)
#     reg_expire_date = models.DateField(blank=True, null=True)
#     commited_volunteers = models.IntegerField(blank=True, null=True)
#     requested_volunteers = models.IntegerField(blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     decline_volunteers = models.IntegerField(blank=True, null=True)
#     tentative_volunteers = models.IntegerField(blank=True, null=True)
#     accepted_volenteers_by_host = models.IntegerField(blank=True, null=True)
#     declined_volenteers_by_host = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'challenge_type'
#         
#     def __str__(self):
#         return str ('challenge_id');
#         
#      
# 
# 
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(User, models.DO_NOTHING)
# 
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
# 
# 
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
# 
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
# 
# 
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
# 
# 
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'django_session'
# 
# 
# class GiftUserType(models.Model):
#     user = models.ForeignKey(User, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
#     activation_key = models.CharField(max_length=45, blank=True, null=True)
#     display_name = models.CharField(max_length=200, blank=True, null=True)
#     alias = models.CharField(max_length=200, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=45, blank=True, null=True)
#     image = models.ImageField(max_length=500, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True) 
#     occupation = models.CharField(max_length=100, blank=True, null=True)
#        
#     class Meta:
#         managed = False
#         db_table = 'gift_user_type'
# 
# class GifterFeedback(models.Model):
#     id = models.IntegerField(primary_key=True)
#     gift_user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='gift_user', blank=True, null=True)
#     user_challenge_category_location = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location', blank=True, null=True)
#     point = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'gifter_feedback'
# 
# 
# class GiftergoalType(models.Model):
#     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     goal_start_date = models.DateField(blank=True, null=True)
#     goal_end_date = models.DateField(blank=True, null=True)
#     goal_hours = models.IntegerField(blank=True, null=True)
#     goal_tasks = models.IntegerField(blank=True, null=True)
#     completed_hours = models.IntegerField(blank=True, null=True)
#     completed_tasks = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'giftergoal_type'
# 
# class HostFeedback(models.Model):
#     gift_user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='gift_user', blank=True, null=True)
#     user_challenge_category_location_rel_rel = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location_rel_rel', blank=True, null=True)
#     point = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'host_feedback'
#         
#         
# class HostUserType(models.Model):
#     organization = models.CharField(max_length=200, blank=True, null=True)
#     contact = models.CharField(max_length=45, blank=True, null=True)
#     website = models.CharField(max_length=200, blank=True, null=True)
#     user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     activation_key=models.CharField(max_length=45, blank=True, null=True)
#     hometown = models.CharField(max_length=60, blank=True, null=True)
#     display_name = models.CharField(max_length=200, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     image = models.ImageField()
#     gender = models.CharField(max_length=45, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     occupation = models.CharField(max_length=100, blank=True, null=True)
#     
#     class Meta:
#         managed = False
#         db_table = 'host_user_type'
# 
# 
# class LocationType(models.Model):
#     id = models.AutoField(primary_key=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     province = models.CharField(max_length=50, blank=True, null=True)
#     lattitude = models.CharField(max_length=45, blank=True, null=True)
#     longitude = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'location_type'
# 
#     def __str__(self):
#         return str(self.city) or u''+" "+str(self.province) or u''
#     
# class MyChallengeRelRel(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_challenge_category_location = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location', blank=True, null=True)
#     is_favourite = models.IntegerField(blank=True, null=True)
#     status = models.ForeignKey('StatusType', models.DO_NOTHING, db_column='status', blank=True, null=True)
#     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     challenge_join_date = models.DateTimeField(default=timezone.now())
# 
#     class Meta:
#         managed = True
#         db_table = 'my_challenge_rel_rel'
# 
# 
# class RankType(models.Model):
#     rank = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'rank_type'
# 
#     def __str__(self):
#         return str(self.rank) or u''
#     
# class StatusType(models.Model):
#     id = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=45)
# 
#     class Meta:
#         managed = False
#         db_table = 'status_type'
# 
#     def __str__(self):
#         return str(self.status) or u''
#         
# class UserCategoryRel(models.Model):
#     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     category = models.ForeignKey(CategoryType, models.DO_NOTHING, db_column='category', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user_category_rel'
# 
# 
# 
# class UserCategoryRelCategory(models.Model):
#     usercategoryrel = models.ForeignKey(UserCategoryRel, models.DO_NOTHING, db_column='usercategoryrel', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user_category_rel_category'
# 
#     
# 
# # class UserChallengeCategoryLocationRelRel(models.Model):
# #     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
# #     #category_location = models.ForeignKey(CategoryLocationRel, models.DO_NOTHING, db_column='category_location', blank=True, null=True)
# #     categorytype=models.ManyToManyField(CategoryType)
# #     locationtype=models.ManyToManyField(LocationType)
# #     challenge = models.ForeignKey(ChallengeType, models.DO_NOTHING, db_column='challenge', blank=True, null=True)
# #     status = models.ForeignKey(StatusType, models.DO_NOTHING, db_column='status', blank=True, null=True)
# #     photo = models.CharField(max_length=500,blank=True, null=True)
# #     photo1 = models.CharField( max_length=500,blank=True, null=True)
# #     class Meta:
# #         managed = False
# #         db_table = 'user_challenge_category_location_rel_rel'
# #      
# #     def __str__(self):
# #         return str(self.challenge.title) or u''
# #     
# #     def __str__(self):
# #         return str(self.photo) or u''   
# 
# 
# class UserChallengeCategoryLocationRelRel(models.Model):
#     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     #category_location = models.ForeignKey(CategoryLocationRel, models.DO_NOTHING, db_column='category_location', blank=True, null=True)
#     categorytype=models.ManyToManyField(CategoryType)
#     locationtype=models.ManyToManyField(LocationType)
#     challenge = models.ForeignKey(ChallengeType, models.DO_NOTHING, db_column='challenge', blank=True, null=True)
#     status = models.ForeignKey(StatusType, models.DO_NOTHING, db_column='status', blank=True, null=True)
#     photo = models.ImageField(blank=True, null=True)
#     photo1 = models.CharField(max_length=500, blank=True, null=True)
#     class Meta:
#         managed = False
#         db_table = 'user_challenge_category_location_rel_rel'
#      
#     def __str__(self):
#         return str(self.challenge.title) or u''
#     
# class UserChallengeImage(models.Model): 
#     challenge = models.ForeignKey(ChallengeType, models.DO_NOTHING, db_column='challenge', blank=True, null=True)   
#     photo = models.CharField(max_length=500,blank=True, null=True)
#     
#      
#      
#     class Meta:
#         managed = False
#         db_table = 'user_challenge_category_location_rel_rel'
#       
#     def __str__(self):
#         return str(self.photo) or u''    
# #     
# 
# 
# class UserChallengeCategoryLocationRelRelCategory(models.Model): 
#     userchallengecategorylocationrelrel =models.ForeignKey(UserChallengeCategoryLocationRelRel, models.DO_NOTHING)
#     categorytype = models.ForeignKey(CategoryType, models.DO_NOTHING)
#     class Meta:
#         managed = False
#         db_table = 'user_challenge_category_location_rel_rel_categorytype'
#         
# class UserChallengeCategoryLocationRelRelLocation(models.Model): 
#     userchallengecategorylocationrelrel =models.ForeignKey(UserChallengeCategoryLocationRelRel, models.DO_NOTHING)
#     categorytype = models.ForeignKey(CategoryType, models.DO_NOTHING)
#     locationtype=models.ForeignKey(LocationType, models.DO_NOTHING)
#     class Meta:
#         managed = False
#         db_table = 'user_challenge_category_location_rel_rel_locationtype'
#     
# 
# 
# class UserType(models.Model):
#     organization = models.CharField(max_length=200, blank=True, null=True)
#     contact = models.CharField(max_length=45, blank=True, null=True)
#     website = models.CharField(max_length=200, blank=True, null=True)
#     user = models.OneToOneField(User, models.DO_NOTHING, db_column='user', primary_key=True)
#     #user = models.OneToOneField(User,primary_key=True)
#     activation_key = models.CharField(max_length=45, blank=True, null=True)
#     hometown = models.CharField(max_length=60, blank=True, null=True)
#     display_name = models.CharField(max_length=200, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     image = models.ImageField(blank=True, null=True)
#     gender = models.CharField(max_length=45, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     alias = models.CharField(max_length=100, blank=True, null=True)
#     occupation = models.CharField(max_length=100, blank=True, null=True)
#     host_permission = models.CharField(max_length=45, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user_type'
# 
# class UserType99(models.Model):
#     organization = models.CharField(max_length=200, blank=True, null=True)
#     contact = models.CharField(max_length=45, blank=True, null=True)
#     website = models.CharField(max_length=200, blank=True, null=True)
#     user = models.OneToOneField(User, models.DO_NOTHING, db_column='user', primary_key=True)
#     #user = models.OneToOneField(User,primary_key=True)
#     activation_key = models.CharField(max_length=45, blank=True, null=True)
#     hometown = models.CharField(max_length=60, blank=True, null=True)
#     display_name = models.CharField(max_length=200, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#    
#     image = models.CharField(max_length=200,blank=True, null=True)
#     gender = models.CharField(max_length=45, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     alias = models.CharField(max_length=100, blank=True, null=True)
#     occupation = models.CharField(max_length=100, blank=True, null=True)
#     host_permission = models.CharField(max_length=45, blank=True, null=True) 
#     
# 
#     class Meta:
#         managed = False
#         db_table = 'user_type'
#     def __str__(self):
#         return str(self.image) or u''    
# 
# 
# 
# class UserLocationRel(models.Model):
#     user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
#     location = models.ForeignKey(LocationType, models.DO_NOTHING, db_column='location', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user_location_rel'
# 
# 
# class UserRankingRel(models.Model):
#     rank = models.ForeignKey(RankType, models.DO_NOTHING, db_column='rank', blank=True, null=True)
#     my_challenge = models.ForeignKey(MyChallengeRelRel, models.DO_NOTHING, db_column='my_challenge', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'user_ranking_rel'
