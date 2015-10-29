# jenkins-jobs-mattermost

Mattermost publisher for jenkins job builder

# Getting started

```yaml
- project:
	name: foo
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
```
