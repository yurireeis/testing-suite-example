from tests.e2e.services.support import save_print, get_webdriver


def before_feature(context, feature):
    pass


def before_all(context):
    context.browser = get_webdriver()
    context.browser.get('https://www.shipay.com.br/')


def after_feature(context, feature):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass
