Prerequisites
Before you begin, make sure your development environment includes Node.js® and an npm package manager.

Node.js
Angular requires Node.js version 8.x or 10.x

To check your version, run node -v in a terminal/console window.
To get Node.js, go to nodejs.org.
Angular CLI
Install the Angular CLI globally using a terminal/console window.

npm install -g @angular/cli
Update to Angular 8
Angular 8 requires Node.js version 12.x
Update guide - see: https://update.angular.io

Installation 
rm -rf node_modules 
install npm
Go to src > app > pages > product-management > product-management.module.ts : import { PaginationModule } from  'ngx-bootstrap/pagination';

Run project 
ng serve -o 

