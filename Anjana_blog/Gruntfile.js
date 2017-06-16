// Load Grunt
module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        // Tasks
        sass: { // Begin Sass Plugin
            options:{
                loadPath: ['bower_components/foundation-sites/scss']
            },
            dist: {
                options: {
                    sourcemap: 'none'
                },
                files: [{
                    expand: true,
                    cwd: 'sass',
                    src: ['**/*.scss'],
                    dest: 'static/css',
                    ext: '.css'
                }]
            }
        },
        postcss: { // Begin Post CSS Plugin
            options: {
                map: false,
                processors: [
                    require('autoprefixer')({
                        browsers: ['last 2 versions']
                    })
                ]
            },
            dist: {
                src: 'static/css/style.css'
            }
        },
        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'static/css',
                    src: ['style.css', '!*.min.css'],
                    dest: 'static/css',
                    ext: '.min.css'
                }]
            }
        },
        uglify: {
            dist: {
                files: {
                    'static/js/jquery.min.js': ['bower_components/jquery/dist/jquery.js'],
                    'static/js/script.min.js': ['src/script.js'],
                    'static/js/foundation.min.js': ['bower_components/foundation-sites/dist/js/foundation.min.js']
                }
            }
        },
        watch: { // Compile everything into one task with Watch Plugin
            options: {
                livereload: true
            },
            css: {
                files: 'sass/*.scss',
                tasks: ['sass', 'postcss', 'cssmin']
            },
            js: {
                files: 'src/*.js',
                tasks: ['uglify']
            }
        },
        connect: {
            server: {
                options: {
                    port: 9000,
                    base: '.',
                    hostname: '0.0.0.0',
                    protocol: 'http',
                    livereload: true,
                    open: true,
                }
            }
        }
    });
    // Load Grunt plugins
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-postcss');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-connect');
    // Register Grunt tasks
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('server', ['connect', 'watch']);
};