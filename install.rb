loop do
	print("Do you want to install the requirements?(y/n): ")
	var = gets.chomp
	if var == 'y'
		system "chmod +x jhonny"
		system "mv jhonny /$PATH/bin/"
		system "sudo apt install python3"
		system "pip install phonenumbers"
		system "pip install json"
		system "pip install time"
		system "pip install phonenumbers"
		system "pip install requests"
		system "pip install pprint"
		system "pip install http.client"
		system "pip install re sys textwrap socket"
		system "pip install lxml"
		system "pip install getpass"
		system "pip install shutil"
		system "echo -e \033[0;49;91m Type\033[m\033[0;49;93m jhonny "
		break
	else
		puts "bye bye"
		break
	end

end
