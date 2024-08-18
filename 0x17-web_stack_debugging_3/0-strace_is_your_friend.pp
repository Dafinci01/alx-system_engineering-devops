# A puppet script to correct a cinfig file

$file_path = '/var/www/html/wp-settings.php'

#replace "phpp" with "php"

exec { 'fix_line':

  command => "sed -i 's/phpp/php/g' ${file_path}",

  path    => ['/bin','/usr/bin']

}
