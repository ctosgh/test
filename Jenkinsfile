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
        sh("export AWS_ACCESS_KEY_ID=AKIAWTNNZ7OS5N7WNF7B; export AWS_SECRET_ACCESS_KEY=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; cd mysam; sam build; sam deploy --no-confirm-changeset")
    }
}
