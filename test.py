Hello world!
748
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CategoryLocationRel(models.Model):
    category = models.ForeignKey('CategoryType', models.DO_NOTHING, db_column='category', blank=True, null=True)
    location = models.ForeignKey('LocationType', models.DO_NOTHING, db_column='location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_location_rel'


class CategoryType(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'category_type'


class CeleryTaskmeta(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celery_taskmeta'


class CeleryTasksetmeta(models.Model):
    taskset_id = models.CharField(unique=True, max_length=255)
    result = models.TextField()
    date_done = models.DateTimeField()
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'celery_tasksetmeta'


class ChallengeCreatorRankingRel(models.Model):
    rank = models.ForeignKey('RankType', models.DO_NOTHING, db_column='rank', blank=True, null=True)
    user_challenge_category_location = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_creator_ranking_rel'


class ChallengeType(models.Model):
    challenge_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    photo = models.CharField(max_length=500, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    venue = models.CharField(max_length=500, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    reg_expire_date = models.DateField(blank=True, null=True)
    commited_volunteers = models.IntegerField(blank=True, null=True)
    requested_volunteers = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    decline_volunteers = models.IntegerField(blank=True, null=True)
    tentative_volunteers = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    accepted_volenteers_by_host = models.IntegerField(blank=True, null=True)
    declined_volenteers_by_host = models.IntegerField(blank=True, null=True)
    direction = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_type'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjceleryCrontabschedule(models.Model):
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month_of_year = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'djcelery_crontabschedule'


class DjceleryIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'djcelery_intervalschedule'


class DjceleryPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjceleryCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjceleryIntervalschedule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_periodictask'


class DjceleryPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'djcelery_periodictasks'


class DjceleryTaskstate(models.Model):
    state = models.CharField(max_length=64)
    task_id = models.CharField(unique=True, max_length=36)
    name = models.CharField(max_length=200, blank=True, null=True)
    tstamp = models.DateTimeField()
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    retries = models.IntegerField()
    hidden = models.IntegerField()
    worker = models.ForeignKey('DjceleryWorkerstate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_taskstate'


class DjceleryWorkerstate(models.Model):
    hostname = models.CharField(unique=True, max_length=255)
    last_heartbeat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_workerstate'


class GiftUserType(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
    activation_key = models.CharField(max_length=45, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    alias = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_user_type'


class GiftergoalType(models.Model):
    user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
    goal_start_date = models.DateField(blank=True, null=True)
    goal_end_date = models.DateField(blank=True, null=True)
    goal_hours = models.IntegerField(blank=True, null=True)
    goal_tasks = models.IntegerField(blank=True, null=True)
    completed_hours = models.IntegerField(blank=True, null=True)
    completed_tasks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giftergoal_type'


class LocationType(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    lattitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_type'


class MyChallengeRelRel(models.Model):
    user_challenge_category_location = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_location', blank=True, null=True)
    is_favourite = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey('StatusType', models.DO_NOTHING, db_column='status', blank=True, null=True)
    user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
    challenge_join_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_challenge_rel_rel'


class Oauth2ProviderAccesstoken(models.Model):
    token = models.CharField(max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    skip_authorization = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    code = models.CharField(max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=255)
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderRefreshtoken(models.Model):
    token = models.CharField(max_length=255)
    access_token = models.ForeignKey(Oauth2ProviderAccesstoken, models.DO_NOTHING, unique=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'


class RankType(models.Model):
    rank = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_type'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StatusType(models.Model):
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'status_type'


class UserCategoryRel(models.Model):
    user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
    category = models.ForeignKey(CategoryType, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_category_rel'


class UserCategoryRelCategory(models.Model):
    usercategoryrel = models.ForeignKey(UserCategoryRel, models.DO_NOTHING, db_column='usercategoryrel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_category_rel_category'


class UserChallengeCategoryLocationMtom(models.Model):
    user_challenge_category_locationrelrel = models.ForeignKey('UserChallengeCategoryLocationRelRel', models.DO_NOTHING, db_column='user_challenge_category_locationrelrel', blank=True, null=True)
    category = models.ForeignKey(CategoryType, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_challenge_category_location_mtom'


class UserChallengeCategoryLocationRelRel(models.Model):
    user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
    challenge = models.ForeignKey(ChallengeType, models.DO_NOTHING, db_column='challenge', blank=True, null=True)
    status = models.ForeignKey(StatusType, models.DO_NOTHING, db_column='status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_challenge_category_location_rel_rel'


class UserChallengeCategoryLocationRelRelCategory(models.Model):
    userchallengecategorylocationrelrel = models.ForeignKey(UserChallengeCategoryLocationRelRel, models.DO_NOTHING, db_column='userchallengecategorylocationrelrel', blank=True, null=True)
    category = models.ForeignKey(CategoryType, models.DO_NOTHING, db_column='category', blank=True, null=True)
    location = models.ForeignKey(LocationType, models.DO_NOTHING, db_column='location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_challenge_category_location_rel_rel_category'


class UserLocationRel(models.Model):
    user = models.ForeignKey(AuthUserGroups, models.DO_NOTHING, db_column='user', blank=True, null=True)
    location = models.ForeignKey(LocationType, models.DO_NOTHING, db_column='location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_location_rel'


class UserRankingRel(models.Model):
    rank = models.ForeignKey(RankType, models.DO_NOTHING, db_column='rank', blank=True, null=True)
    my_challenge = models.ForeignKey(MyChallengeRelRel, models.DO_NOTHING, db_column='my_challenge', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ranking_rel'


class UserType(models.Model):
    organization = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', primary_key=True)
    activation_key = models.CharField(max_length=45, blank=True, null=True)
    hometown = models.CharField(max_length=60, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    host_permission = models.CharField(max_length=45, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type'
