import xml.etree.ElementTree as XML


def slack_properties(parser, xml_parent, data):
    """yaml: slack

    Example::

      properties:
        - slack:
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
            include-custom-message: true
            room: '#jenkins'
            token: secret
            team-domain: example.com
            custom-message: message
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.slack.SlackNotifier_-SlackJobProperty')
    notifier.set('plugin', 'slack@1.8')

    for opt, attr in (('notify-start', 'startNotification'),
                      ('notify-success', 'notifySuccess'),
                      ('notify-aborted', 'notifyAborted'),
                      ('notify-notbuilt', 'notifyNotBuilt'),
                      ('notify-unstable', 'notifyUnstable'),
                      ('notify-failure', 'notifyFailure'),
                      ('notify-backtonormal', 'notifyBackToNormal'),
                      ('notify-repeatedfailure', 'notifyRepeatedFailure'),
                      ('include-test-summary', 'includeTestSummary'),
                      ('show-commit-list', 'showCommitList'),
                      ('include-custom-message', 'includeCustomMessage')):
        (XML.SubElement(notifier, attr)
         .text) = 'true' if data.get(opt, True) else 'false'

    for opt, attr in (('team-domain', 'teamDomain'),
                      ('token', 'token'),
                      ('room', 'room')):
        (XML.SubElement(notifier, attr)
         .text) = data.get(opt)

    if data.get('include-custom-message'):
        (XML.SubElement(notifier, 'customMessage')
         .text) = data.get('custom-message')


def slack_publisher(parser, xml_parent, data):
    """yaml: slack

    Example::

      publishers:
        - slack:
            team-domain: example.com
            auth-token: secret
            build-server-url: https://jenkins.example.com
            room: '#jenkins'
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.slack.SlackNotifier')
    notifier.set('plugin', 'slack@1.8')

    for (opt, attr) in (('team-domain', 'teamDomain'),
                        ('auth-token', 'authToken'),
                        ('build-server-url', 'buildServerUrl'),
                        ('room', 'room')):
        XML.SubElement(notifier, attr).text = data.get(opt, '')
