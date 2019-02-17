from jira import JIRA

jac = JIRA(basic_auth=('twister42@inbox.ru', '!Qw2#er4'), options={'server': 'https://twister42v001.atlassian.net'})
# project = jac.project('testAPI')
projects = jac.projects()
sprint = jac.sprint(1)
issue = jac.issue('TES-1')

print(sprint)
print(issue.fields.project.key)
print(issue.fields.description)


