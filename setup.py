from setuptools import setup

setup(
    name='jenkins-jobs-slack',
    version='0.3.2',
    description='Jenkins Job Builder Slack Notifier',
    url='https://github.com/asmundg/jenkins-jobs-slack',
    author='Aasmund Grammeltvedt',
    author_email='asmundg@big-oil.org',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.properties': [
            'slack = jenkins_jobs_slack.slack:slack_properties'],
        'jenkins_jobs.publishers': [
            'slack = jenkins_jobs_slack.slack:slack_publisher']},
    packages=['jenkins_jobs_slack'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
