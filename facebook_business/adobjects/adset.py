# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker
from facebook_business.mixins import HasAdLabels
from facebook_business.mixins import CanValidate

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdSet(
    AbstractCrudObject,
    HasAdLabels,
    CanValidate,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdSet = True
        super(AdSet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        ad_keywords = 'ad_keywords'
        adlabels = 'adlabels'
        adset_schedule = 'adset_schedule'
        asset_feed_id = 'asset_feed_id'
        attribution_spec = 'attribution_spec'
        best_creative = 'best_creative'
        bid_adjustments = 'bid_adjustments'
        bid_amount = 'bid_amount'
        bid_constraints = 'bid_constraints'
        bid_info = 'bid_info'
        bid_strategy = 'bid_strategy'
        billing_event = 'billing_event'
        budget_remaining = 'budget_remaining'
        campaign = 'campaign'
        campaign_id = 'campaign_id'
        configured_status = 'configured_status'
        created_time = 'created_time'
        creative_sequence = 'creative_sequence'
        daily_budget = 'daily_budget'
        daily_min_spend_target = 'daily_min_spend_target'
        daily_spend_cap = 'daily_spend_cap'
        destination_type = 'destination_type'
        effective_status = 'effective_status'
        end_time = 'end_time'
        frequency_control_specs = 'frequency_control_specs'
        full_funnel_exploration_mode = 'full_funnel_exploration_mode'
        id = 'id'
        instagram_actor_id = 'instagram_actor_id'
        is_dynamic_creative = 'is_dynamic_creative'
        issues_info = 'issues_info'
        lifetime_budget = 'lifetime_budget'
        lifetime_imps = 'lifetime_imps'
        lifetime_min_spend_target = 'lifetime_min_spend_target'
        lifetime_spend_cap = 'lifetime_spend_cap'
        name = 'name'
        optimization_goal = 'optimization_goal'
        pacing_type = 'pacing_type'
        promoted_object = 'promoted_object'
        recommendations = 'recommendations'
        recurring_budget_semantics = 'recurring_budget_semantics'
        review_feedback = 'review_feedback'
        rf_prediction_id = 'rf_prediction_id'
        source_adset = 'source_adset'
        source_adset_id = 'source_adset_id'
        start_time = 'start_time'
        status = 'status'
        targeting = 'targeting'
        time_based_ad_rotation_id_blocks = 'time_based_ad_rotation_id_blocks'
        time_based_ad_rotation_intervals = 'time_based_ad_rotation_intervals'
        updated_time = 'updated_time'
        use_new_app_click = 'use_new_app_click'
        campaign_spec = 'campaign_spec'
        daily_imps = 'daily_imps'
        date_format = 'date_format'
        execution_options = 'execution_options'
        line_number = 'line_number'
        rb_prediction_id = 'rb_prediction_id'
        time_start = 'time_start'
        time_stop = 'time_stop'
        topline_id = 'topline_id'
        upstream_events = 'upstream_events'

    class BidStrategy:
        lowest_cost_without_cap = 'LOWEST_COST_WITHOUT_CAP'
        lowest_cost_with_bid_cap = 'LOWEST_COST_WITH_BID_CAP'
        target_cost = 'TARGET_COST'

    class BillingEvent:
        app_installs = 'APP_INSTALLS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        thruplay = 'THRUPLAY'
        video_views = 'VIDEO_VIEWS'

    class ConfiguredStatus:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        deleted = 'DELETED'
        paused = 'PAUSED'

    class EffectiveStatus:
        active = 'ACTIVE'
        adset_paused = 'ADSET_PAUSED'
        archived = 'ARCHIVED'
        campaign_paused = 'CAMPAIGN_PAUSED'
        deleted = 'DELETED'
        disapproved = 'DISAPPROVED'
        paused = 'PAUSED'
        pending_billing_info = 'PENDING_BILLING_INFO'
        pending_review = 'PENDING_REVIEW'
        preapproved = 'PREAPPROVED'
        with_issues = 'WITH_ISSUES'

    class OptimizationGoal:
        ad_recall_lift = 'AD_RECALL_LIFT'
        app_downloads = 'APP_DOWNLOADS'
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        clicks = 'CLICKS'
        derived_events = 'DERIVED_EVENTS'
        engaged_users = 'ENGAGED_USERS'
        event_responses = 'EVENT_RESPONSES'
        impressions = 'IMPRESSIONS'
        landing_page_views = 'LANDING_PAGE_VIEWS'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        offsite_conversions = 'OFFSITE_CONVERSIONS'
        page_engagement = 'PAGE_ENGAGEMENT'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        reach = 'REACH'
        replies = 'REPLIES'
        social_impressions = 'SOCIAL_IMPRESSIONS'
        thruplay = 'THRUPLAY'
        two_second_continuous_video_views = 'TWO_SECOND_CONTINUOUS_VIDEO_VIEWS'
        value = 'VALUE'
        video_views = 'VIDEO_VIEWS'

    class Status:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        deleted = 'DELETED'
        paused = 'PAUSED'

    class DatePreset:
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_90d = 'last_90d'
        last_month = 'last_month'
        last_quarter = 'last_quarter'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_year = 'last_year'
        lifetime = 'lifetime'
        this_month = 'this_month'
        this_quarter = 'this_quarter'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'
        today = 'today'
        yesterday = 'yesterday'

    class DestinationType:
        app = 'APP'
        applinks_automatic = 'APPLINKS_AUTOMATIC'
        messenger = 'MESSENGER'
        undefined = 'UNDEFINED'
        website = 'WEBSITE'

    class ExecutionOptions:
        include_recommendations = 'include_recommendations'
        validate_only = 'validate_only'

    class FullFunnelExplorationMode:
        extended_exploration = 'EXTENDED_EXPLORATION'
        limited_exploration = 'LIMITED_EXPLORATION'
        none_exploration = 'NONE_EXPLORATION'

    class Operator:
        all = 'ALL'
        any = 'ANY'

    class StatusOption:
        active = 'ACTIVE'
        inherited_from_source = 'INHERITED_FROM_SOURCE'
        paused = 'PAUSED'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adsets'

    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_set(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'am_call_tags': 'map',
            'date_preset': 'date_preset_enum',
            'from_adtable': 'bool',
            'time_range': 'Object',
        }
        enums = {
            'date_preset_enum': [
                'last_14d',
                'last_28d',
                'last_30d',
                'last_3d',
                'last_7d',
                'last_90d',
                'last_month',
                'last_quarter',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_year',
                'lifetime',
                'this_month',
                'this_quarter',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
                'today',
                'yesterday',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'account_id': 'string',
            'ad_keywords': 'Object',
            'adlabels': 'list<Object>',
            'bid_amount': 'int',
            'bid_adjustments': 'Object',
            'bid_constraints': 'map<string, Object>',
            'bid_strategy': 'bid_strategy_enum',
            'billing_event': 'billing_event_enum',
            'campaign_spec': 'Object',
            'adset_schedule': 'list<Object>',
            'status': 'status_enum',
            'creative_sequence': 'list<string>',
            'daily_budget': 'unsigned int',
            'daily_imps': 'unsigned int',
            'daily_min_spend_target': 'unsigned int',
            'daily_spend_cap': 'unsigned int',
            'date_format': 'string',
            'destination_type': 'destination_type_enum',
            'end_time': 'datetime',
            'execution_options': 'list<execution_options_enum>',
            'lifetime_budget': 'unsigned int',
            'lifetime_imps': 'unsigned int',
            'lifetime_min_spend_target': 'unsigned int',
            'lifetime_spend_cap': 'unsigned int',
            'name': 'string',
            'optimization_goal': 'optimization_goal_enum',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'rb_prediction_id': 'string',
            'rf_prediction_id': 'string',
            'start_time': 'datetime',
            'targeting': 'Targeting',
            'time_based_ad_rotation_id_blocks': 'list<list<unsigned int>>',
            'time_based_ad_rotation_intervals': 'list<unsigned int>',
            'time_start': 'datetime',
            'time_stop': 'datetime',
            'upstream_events': 'map',
            'full_funnel_exploration_mode': 'full_funnel_exploration_mode_enum',
            'attribution_spec': 'list<map>',
        }
        enums = {
            'bid_strategy_enum': AdSet.BidStrategy.__dict__.values(),
            'billing_event_enum': AdSet.BillingEvent.__dict__.values(),
            'status_enum': AdSet.Status.__dict__.values(),
            'destination_type_enum': AdSet.DestinationType.__dict__.values(),
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
            'optimization_goal_enum': AdSet.OptimizationGoal.__dict__.values(),
            'full_funnel_exploration_mode_enum': AdSet.FullFunnelExplorationMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_activities(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adactivity import AdActivity
        param_types = {
            'after': 'string',
            'limit': 'int',
            'since': 'datetime',
            'category': 'category_enum',
            'until': 'datetime',
            'uid': 'int',
            'business_id': 'string',
        }
        enums = {
            'category_enum': AdActivity.Category.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/activities',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdActivity,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdActivity, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_studies(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adstudy import AdStudy
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_studies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_creatives(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adcreative import AdCreative
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adcreatives',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_ad_labels(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
        }
        enums = {
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_label(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
        }
        enums = {
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_rules_governed(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adrule import AdRule
        param_types = {
            'pass_evaluation': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adrules_governed',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdRule, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ads(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'include_deleted': 'bool',
            'effective_status': 'list<string>',
            'date_preset': 'date_preset_enum',
            'time_range': 'Object',
            'updated_since': 'int',
            'ad_draft_id': 'string',
        }
        enums = {
            'date_preset_enum': Ad.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Ad, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_async_ad_requests(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
        param_types = {
            'statuses': 'list<statuses_enum>',
        }
        enums = {
            'statuses_enum': AdAsyncRequest.Statuses.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asyncadrequests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAsyncRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAsyncRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_copies(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'effective_status': 'list<effective_status_enum>',
            'date_preset': 'date_preset_enum',
            'is_completed': 'bool',
            'time_range': 'Object',
        }
        enums = {
            'effective_status_enum': AdSet.EffectiveStatus.__dict__.values(),
            'date_preset_enum': AdSet.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/copies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_copy(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'deep_copy': 'bool',
            'campaign_id': 'string',
            'rename_options': 'Object',
            'status_option': 'status_option_enum',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'create_dco_adset': 'bool',
        }
        enums = {
            'status_option_enum': AdSet.StatusOption.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/copies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_delivery_estimate(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adcampaigndeliveryestimate import AdCampaignDeliveryEstimate
        param_types = {
            'targeting_spec': 'Targeting',
            'optimization_goal': 'optimization_goal_enum',
            'promoted_object': 'Object',
        }
        enums = {
            'optimization_goal_enum': AdCampaignDeliveryEstimate.OptimizationGoal.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/delivery_estimate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCampaignDeliveryEstimate,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCampaignDeliveryEstimate, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adsinsights import AdsInsights
        if is_async:
          return self.get_insights_async(fields, params, batch, success, failure, pending)
        param_types = {
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsInsights,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsInsights, api=self._api),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_insights_async(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adreportrun import AdReportRun
        from facebook_business.adobjects.adsinsights import AdsInsights
        param_types = {
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportRun,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdReportRun, api=self._api),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_targeting_sentence_lines(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingsentencelines',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=TargetingSentenceLine,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=TargetingSentenceLine, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'account_id': 'string',
        'ad_keywords': 'AdKeywords',
        'adlabels': 'list<AdLabel>',
        'adset_schedule': 'list<DayPart>',
        'asset_feed_id': 'string',
        'attribution_spec': 'list<AttributionSpec>',
        'best_creative': 'AdDynamicCreative',
        'bid_adjustments': 'AdBidAdjustments',
        'bid_amount': 'unsigned int',
        'bid_constraints': 'AdCampaignBidConstraint',
        'bid_info': 'map<string, unsigned int>',
        'bid_strategy': 'BidStrategy',
        'billing_event': 'BillingEvent',
        'budget_remaining': 'string',
        'campaign': 'Campaign',
        'campaign_id': 'string',
        'configured_status': 'ConfiguredStatus',
        'created_time': 'datetime',
        'creative_sequence': 'list<string>',
        'daily_budget': 'string',
        'daily_min_spend_target': 'string',
        'daily_spend_cap': 'string',
        'destination_type': 'string',
        'effective_status': 'EffectiveStatus',
        'end_time': 'datetime',
        'frequency_control_specs': 'list<AdCampaignFrequencyControlSpecs>',
        'full_funnel_exploration_mode': 'string',
        'id': 'string',
        'instagram_actor_id': 'string',
        'is_dynamic_creative': 'bool',
        'issues_info': 'list<AdCampaignIssuesInfo>',
        'lifetime_budget': 'string',
        'lifetime_imps': 'int',
        'lifetime_min_spend_target': 'string',
        'lifetime_spend_cap': 'string',
        'name': 'string',
        'optimization_goal': 'OptimizationGoal',
        'pacing_type': 'list<string>',
        'promoted_object': 'AdPromotedObject',
        'recommendations': 'list<AdRecommendation>',
        'recurring_budget_semantics': 'bool',
        'review_feedback': 'string',
        'rf_prediction_id': 'string',
        'source_adset': 'AdSet',
        'source_adset_id': 'string',
        'start_time': 'datetime',
        'status': 'Status',
        'targeting': 'Targeting',
        'time_based_ad_rotation_id_blocks': 'list<list<int>>',
        'time_based_ad_rotation_intervals': 'list<unsigned int>',
        'updated_time': 'datetime',
        'use_new_app_click': 'bool',
        'campaign_spec': 'Object',
        'daily_imps': 'unsigned int',
        'date_format': 'string',
        'execution_options': 'list<ExecutionOptions>',
        'line_number': 'unsigned int',
        'rb_prediction_id': 'string',
        'time_start': 'datetime',
        'time_stop': 'datetime',
        'topline_id': 'string',
        'upstream_events': 'map',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BidStrategy'] = AdSet.BidStrategy.__dict__.values()
        field_enum_info['BillingEvent'] = AdSet.BillingEvent.__dict__.values()
        field_enum_info['ConfiguredStatus'] = AdSet.ConfiguredStatus.__dict__.values()
        field_enum_info['EffectiveStatus'] = AdSet.EffectiveStatus.__dict__.values()
        field_enum_info['OptimizationGoal'] = AdSet.OptimizationGoal.__dict__.values()
        field_enum_info['Status'] = AdSet.Status.__dict__.values()
        field_enum_info['DatePreset'] = AdSet.DatePreset.__dict__.values()
        field_enum_info['DestinationType'] = AdSet.DestinationType.__dict__.values()
        field_enum_info['ExecutionOptions'] = AdSet.ExecutionOptions.__dict__.values()
        field_enum_info['FullFunnelExplorationMode'] = AdSet.FullFunnelExplorationMode.__dict__.values()
        field_enum_info['Operator'] = AdSet.Operator.__dict__.values()
        field_enum_info['StatusOption'] = AdSet.StatusOption.__dict__.values()
        return field_enum_info


