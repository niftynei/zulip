# -*- coding: utf-8 -*-
from zerver.lib.test_classes import WebhookTestCase

class GoSquaredHookTests(WebhookTestCase):
    STREAM_NAME = 'gosquared'
    URL_TEMPLATE = "/api/v1/external/gosquared?stream={stream}&api_key={api_key}"
    FIXTURE_DIR_NAME = 'gosquared'

    # Note: Include a test function per each distinct message condition your integration supports
    def test_traffic_message(self):
        # type: () -> None
        expected_subject = u"GoSquared"
        expected_message = u"requestb.in has 0 visitors online."

        # use fixture named helloworld_hello
        self.send_and_test_stream_message('traffic_spike', expected_subject, expected_message,
                                          content_type="application/x-www-form-urlencoded")