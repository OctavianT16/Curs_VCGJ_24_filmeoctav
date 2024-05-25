/*Jenkins*/

pipeline {

    agent any



    stages {

        stage('Build') {

            agent any

            steps {

                echo 'Building...'

                sh '''

                    pwd;

                    ls -l;

                    . ./activeaza_venv_jenkins

                    '''

            }

        }

        

        /*stage('Testare') {

            problema rulare in paralel, al doilea stage nu mai poate porni venv-ul

            parallel {

         */

         

         

        stage('pylint - calitate cod') {

            agent any

            steps {

                sh '''

                    . ./activeaza_venv;

                    echo '\n\nVerificare lib/biblioteca_filme.py cu pylint\n';

                    pylint --exit-zero lib/biblioteca_filme.py;



                    echo '\n\nVerificare filme.py cu pylint';

                    pylint --exit-zero filme.py;

                '''

            }

        }

        



	

        stage('Unit Testing cu pytest') {

            agent any

            steps {

                echo 'Unit testing with Pytest...'

                sh '''

                    . ./activeaza_venv;

                    flask --app filme test;

                    

                '''

            }

        }

      

        

        stage('Deploy') {

            agent any

            steps {

                echo "Build ID: ${BUILD_NUMBER}"

                echo "Creare imagine docker"

                sh '''

                    docker build -t filme:v${BUILD_NUMBER} .

                    docker create --name filme${BUILD_NUMBER} -p 8020:5011 filme:v${BUILD_NUMBER}

                '''

            }

        }

    }

}


