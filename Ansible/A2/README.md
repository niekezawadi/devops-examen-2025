In deze opdracht maak ik een eigen Ansible-playbook dat een extra functionaliteit toevoegt aan mijn bestaande Apache-webserver op 192.0.2.3.
Ik creëer een custom HTML-pagina via Ansible en valideer deze via de browser.

Alle screenshots staan in:

Ansible/A2/screenshots/
Playbook: custom_webpage_playbook.yaml
Dit playbook maakt een eigen HTML-pagina op de webserver en herstart Apache.

---
- hosts: webservers
  become: yes

  tasks:
    - name: CREATE CUSTOM HTML PAGE
      copy:
        dest: /var/www/html/custom.html
        content: "<h1>Hallo, dit is mijn eigen Ansible experiment!</h1>"

    - name: RESTART APACHE
      service:
        name: apache2
        state: restarted
Screenshot: A2-01-custom-playbook.png

Playbook uitvoeren
Ik voer het playbook uit met:

ansible-playbook -v custom_webpage_playbook.yaml
Screenshot: A2-02-playbook-output.png

Validatie in de browser
Ik open de custom pagina via:

http://192.0.2.3:8081/custom.html

De pagina toont de tekst uit het playbook.

Screenshot: A2-03-browser-custom-page.png

Conclusie
In deze opdracht heb ik:

een eigen Ansible-playbook geschreven

een custom HTML-pagina uitgerold via Ansible

Apache automatisch laten herstarten

de werking gevalideerd via de browser

Dit toont dat ik zelfstandig Ansible-playbooks kan ontwerpen en uitvoeren
