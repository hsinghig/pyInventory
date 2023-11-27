import dateutil, datetime
#  @app.template_filter('strftime')
# def _jinja2_filter_datetime(strDate, fmt=None):
#         date = dateutil.parser.parse(strDate)
#         native = date.replace(tzinfo=None)
#         format='%b %d, %Y %H:%M:%S'
#         format2 = '%Y-%m-%d %H:%M:%S'
#         return native.strftime(format)

def strftime(strDate, fmt=None):
    date = dateutil.parser.parse(strDate)
    native = date.replace(tzinfo=None)
    format='%b %d, %Y %H:%M:%S'
    format2 = '%Y-%m-%d %H:%M:%S'
    return native.strftime(format)