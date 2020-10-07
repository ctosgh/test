node('master'){
    stage('checkout'){
        echo "Checkout code now"
        //git(branch:"master", credentialsId:"1sgh@github1", url:"https://github.com/ctosgh/test.git")
        git(branch:"master", url:"https://github.com/ctosgh/test.git")
    }
        
    stage('stage2'){
        echo "this is stage 2"
        sh("echo ${BRANCH_NAME}")
    }
        
    stage('deploy'){
        sh("cd mysam; sam build; sam deploy --no-confirm-changeset")
    }
}
