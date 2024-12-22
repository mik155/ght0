const github = require('@actions/github')
const core = require('@actions/core')
const exec = require('@actions/exec')

function run() {
    const bucket = core.getInput('bucket', { required: true })
    const region = core.getInput('region', { required: true })
    const folder = core.getInput('folder', { required: true })

    core.notice('Hellow form js action !')
    core.notice(`bucket, region, folder: ${bucket}, ${region}, ${folder}`)

    core.setOutput('website-url', "https://github.com")
}

run();