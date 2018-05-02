#!/usr/bin/env bash

LOCAL_REPO_DIR="${BITBUCKET_REPO_SLUG}-${BITBUCKET_BRANCH}"

ssh deploy@${DEPLOY_SERVER} << EOF

echo ${DEPLOY_SERVER}
echo ${REPO_URL}
echo ${LOCAL_REPO_DIR}

rm -rf ${LOCAL_REPO_DIR}
git clone ${REPO_URL} ${LOCAL_REPO_DIR}
cd ${LOCAL_REPO_DIR}
git checkout ${BITBUCKET_BRANCH}

docker-compose down -v
docker-compose up -d --build

EOF