const github = require('@actions/github')
const core = require('@actions/core')
const exec = require('@action/exec')

function run() {
    core.notice('Hellow form js action !')
}

run();