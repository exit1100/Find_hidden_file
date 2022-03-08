file_signature = ['ff d8 ff e0',
                  'ff d8 ff e8',
                  '89 50 4e 47 0d 0a 1a 0a',
                  '50 4b 03 04',
                  '47 49 46 38 37 61',
                  '47 49 46 38 39 61',
                  '25 50 44 46 2d 31 2e',
                  ]

file_header_footer = {'ff d8 ff e0':'ff d9',
                      'ff d8 ff e8':'ff d9',
                      '89 50 4e 47 0d 0a 1a 0a':'49 45 4e 44 ae 42 60 82',
                      '50 4b 03 04':'50 4b 05 06',
                      '47 49 46 38 37 61':'00 3b',
                      '47 49 46 38 39 61':'00 3b',
                      '25 50 44 46 2d 31 2e':'25 25 45 4f 46'  
                      }

file_extension = {'ff d8 ff e0':'jpeg', 
                  'ff d8 ff e8':'jpeg',
                  '89 50 4e 47 0d 0a 1a 0a':'png',
                  '50 4b 03 04':'zip',
                  '47 49 46 38 37 61':'gif',
                  '47 49 46 38 39 61':'gif',
                  '25 50 44 46 2d 31 2e':'pdf'
                    }