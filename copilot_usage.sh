# #!/bin/bash
# echo "Hello, World!"


# curl -L \
#   -H "Accept: application/vnd.github+json" \
#   -H "Authorization: Bearer <YOUR-TOKEN>" \
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   https://api.github.com/enterprises/ENTERPRISE/copilot/usage

# // javascript
# // Octokit.js
# // https://github.com/octokit/core.js#readme
# const octokit = new Octokit({
#   auth: 'YOUR-TOKEN'
# })

# await octokit.request('GET /enterprises/{enterprise}/copilot/usage', {
#   enterprise: 'ENTERPRISE',
#   headers: {
#     'X-GitHub-Api-Version': '2022-11-28'
#   }
# })

# # GitHub CLI api
# # https://cli.github.com/manual/gh_api

# gh api \
#   -H "Accept: application/vnd.github+json" \
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   /enterprises/ENTERPRISE/copilot/usage

# # response schema:
# {
#   "type": "array",
#   "items": {
#     "title": "Copilot Usage Metrics",
#     "description": "Summary of Copilot usage.",
#     "type": "object",
#     "properties": {
#       "day": {
#         "type": "string",
#         "format": "date",
#         "description": "The date for which the usage metrics are reported, in `YYYY-MM-DD` format."
#       },
#       "total_suggestions_count": {
#         "type": "integer",
#         "description": "The total number of Copilot code completion suggestions shown to users."
#       },
#       "total_acceptances_count": {
#         "type": "integer",
#         "description": "The total number of Copilot code completion suggestions accepted by users."
#       },
#       "total_lines_suggested": {
#         "type": "integer",
#         "description": "The total number of lines of code completions suggested by Copilot."
#       },
#       "total_lines_accepted": {
#         "type": "integer",
#         "description": "The total number of lines of code completions accepted by users."
#       },
#       "total_active_users": {
#         "type": "integer",
#         "description": "The total number of users who were shown Copilot code completion suggestions during the day specified."
#       },
#       "total_chat_acceptances": {
#         "type": "integer",
#         "description": "The total instances of users who accepted code suggested by Copilot Chat in the IDE (panel and inline)."
#       },
#       "total_chat_turns": {
#         "type": "integer",
#         "description": "The total number of chat turns (prompt and response pairs) sent between users and Copilot Chat in the IDE."
#       },
#       "total_active_chat_users": {
#         "type": "integer",
#         "description": "The total number of users who interacted with Copilot Chat in the IDE during the day specified."
#       },
#       "breakdown": {
#         "type": [
#           "array",
#           "null"
#         ],
#         "description": "Breakdown of Copilot code completions usage by language and editor",
#         "items": {
#           "type": "object",
#           "description": "Breakdown of Copilot usage by editor for this language",
#           "additionalProperties": true,
#           "properties": {
#             "language": {
#               "type": "string",
#               "description": "The language in which Copilot suggestions were shown to users in the specified editor."
#             },
#             "editor": {
#               "type": "string",
#               "description": "The editor in which Copilot suggestions were shown to users for the specified language."
#             },
#             "suggestions_count": {
#               "type": "integer",
#               "description": "The number of Copilot suggestions shown to users in the editor specified during the day specified."
#             },
#             "acceptances_count": {
#               "type": "integer",
#               "description": "The number of Copilot suggestions accepted by users in the editor specified during the day specified."
#             },
#             "lines_suggested": {
#               "type": "integer",
#               "description": "The number of lines of code suggested by Copilot in the editor specified during the day specified."
#             },
#             "lines_accepted": {
#               "type": "integer",
#               "description": "The number of lines of code accepted by users in the editor specified during the day specified."
#             },
#             "active_users": {
#               "type": "integer",
#               "description": "The number of users who were shown Copilot completion suggestions in the editor specified during the day specified."
#             }
#           }
#         }
#       }
#     },
#     "required": [
#       "day",
#       "breakdown"
#     ],
#     "additionalProperties": false
#   }
# }

# write a script that hits the Copilot telemetry api and returns metrics

#!/bin/bash

# Get the Copilot usage metrics for an enterprise
# Usage: ./copilot_usage.sh <ENTERPRISE> <TOKEN>
# Example: ./copilot_usage.sh my-enterprise my-token

# Set the enterprise and token
ENTERPRISE=$1
TOKEN=$2

# Get the Copilot usage metrics
curl -s -H "Accept: application/vnd.github+json" \
  -H

  

