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
    notifier.set('plugin', 'slac@1.2')

    for opt, attr in (('notify-start', 'startNotification'),
                      ('notify-success', 'notifySuccess'),
                      ('notify-aborted', 'notifyAborted'),
                      ('notify-notbuilt', 'notifyNotBuilt'),
                      ('notify-unstable', 'notifyUnstable'),
                      ('notify-failure', 'notifyFailure'),
                      ('notify-backtonormal', 'notifyBackToNormal')):
        (XML.SubElement(notifier, attr)
         .text) = data.get(opt, True) and 'true' or 'false'


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

    notifier = XML.SubElement(
        xml_parent, 'jenkins.plugins.slack.SlackNotifier')
    notifier.set('plugin', 'slac@1.2')

    for (opt, attr) in (('team-domain', 'teamDomain'),
                        ('auth-token', 'authToken'),
                        ('build-server-url', 'buildServerUrl'),
                        ('room', 'room')):
        XML.SubElement(notifier, attr).text = data.get(opt, '')
