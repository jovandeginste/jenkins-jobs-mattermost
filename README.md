# jenkins-jobs-slack

Slack publisher and config for jenkins job builder

# Getting started

    - project:
      name: foo
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
            room: '#jenkins'
            token: secret
            team-domain: example.com
            custom-message: message

      publishers:
        - slack:
            team-domain: example.com
            auth-token: secret
            build-server-url: https://jenkins.example.com
            room: '#jenkins'
