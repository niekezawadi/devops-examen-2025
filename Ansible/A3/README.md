In deze opdracht maak ik een tweede eigen Ansible-playbook, maar deze keer op een andere server dan in A1 en A2.
Voor A3 gebruik ik het IP-adres 192.0.2.4.
Ik installeer Nginx via een eigen playbook en valideer de installatie via de browser.

Alle screenshots staan in:

Ansible/A3/screenshots/

#Hosts-bestand aanpassen

Ik voeg de tweede server toe aan het hosts-bestand:
[otherserver]
192.0.2.4 ansible_ssh_user=devasc ansible_ssh_pass=Cisco123!
Screenshot: A3-01-hosts-file.png

#Verbinding testen met de tweede server
Ik test de verbinding met:

ansible otherserver -m ping

Dit geeft een succesvolle pong terug.

Screenshot: A3-02-ping-otherserver.png

#Playbook: install_nginx_playbook.yaml
Dit playbook installeert Nginx op de tweede server en start de service.
---
- hosts: otherserver
  become: yes

  tasks:
    - name: INSTALL NGINX
      apt:
        name: nginx
        state: latest
        update_cache: yes

    - name: START NGINX
      service:
        name: nginx
        state: started

#Playbook uitvoeren
Ik voer het playbook uit met:
ansible-playbook -v install_nginx_playbook.yaml

Screenshot: A3-03-nginx-playbook-output.png

#Validatie in de browser
Ik open de Nginx default page via:

http://192.0.2.4

De standaard Nginx-pagina wordt correct weergegeven.

Screenshot: A3-04-browser-nginx.png

#Conclusie
In deze opdracht heb ik:

een tweede eigen Ansible-playbook gemaakt

een andere server gebruikt dan in A1 en A2

Nginx geïnstalleerd en gestart via Ansible

de werking gevalideerd via de browser
