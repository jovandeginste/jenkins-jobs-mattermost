import xml.etree.ElementTree as XML

def mattermost_publisher(parser, xml_parent, data):
    """yaml: mattermost

    Example::

      publishers:
        - mattermost:
            notify-start: true
            notify-success: true
            notify-aborted: true
            notify-notbuilt: true
            notify-unstable: true
            notify-failure: true
            notify-backtonormal: true
            notify-repeatedfailure: true
            include-test-summary: true
            show-commit-list: true
            endpoint: example.com
            room: '#jenkins'
						icon: 'http://url.to/image.png'
            custom-message: message
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.mattermost.MattermostNotifier')
    notifier.set('plugin', '@1.0')

    for opt, attr in (('notify-start', 'startNotification'),
                      ('notify-success', 'notifySuccess'),
                      ('notify-aborted', 'notifyAborted'),
                      ('notify-notbuilt', 'notifyNotBuilt'),
                      ('notify-unstable', 'notifyUnstable'),
                      ('notify-failure', 'notifyFailure'),
                      ('notify-backtonormal', 'notifyBackToNormal'),
                      ('notify-repeatedfailure', 'notifyRepeatedFailure'),
                      ('include-test-summary', 'includeTestSummary'),
                      ('show-commit-list', 'showCommitList')):
        (XML.SubElement(notifier, attr)
         .text) = 'true' if data.get(opt, True) else 'false'

    for opt, attr in (('endpoint', 'endpoint'),
                      ('room', 'room'),
                      ('icon', 'icon')):
        (XML.SubElement(notifier, attr)
         .text) = data.get(opt)

    if data.get('include-custom-message'):
        (XML.SubElement(notifier, 'includeCustomMessage')
         .text) = 'true'
        (XML.SubElement(notifier, 'customMessage')
         .text) = data.get('custom-message')
    else:
        (XML.SubElement(notifier, 'includeCustomMessage')
         .text) = 'false'
        (XML.SubElement(notifier, 'customMessage')
         .text) = ''
