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
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.slack.SlackNotifier_-SlackJobProperty')
    notifier.set('plugin', 'slack@1.7')

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

    XML.SubElement(notifier, 'teamDomain').text = data.get('team-domain')
    XML.SubElement(notifier, 'token').text = data.get('token')
    XML.SubElement(notifier, 'room').text = data.get('room')


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
    notifier.set('plugin', 'slack@1.7')

    for (opt, attr) in (('team-domain', 'teamDomain'),
                        ('auth-token', 'authToken')):
        XML.SubElement(notifier, attr).text = data.get(opt, '')
