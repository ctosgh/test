node('master'){
    stage('checkout'){
        echo "Checkout code now"
        //git(branch:"master", credentialsId:"1sgh@github1", url:"https://github.com/ctosgh/test.git")
        git(branch:"master", url:"https://github.com/ctosgh/test.git")
    }
        
    stage('stage2'){
        echo "this is stage 2"
    }
        
    stage('deploy'){
        sh("export AWS_ACCESS_KEY_ID=AKIAWTNNZ7OS4RB2YLOJ; export AWS_SECRET_ACCESS_KEY=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; python3 run.py")
    }
}
