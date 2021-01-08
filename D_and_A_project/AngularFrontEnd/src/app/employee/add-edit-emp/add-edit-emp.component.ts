import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-emp',
  templateUrl: './add-edit-emp.component.html',
  styleUrls: ['./add-edit-emp.component.css']
})
export class AddEditEmpComponent implements OnInit {

  constructor(private service:SharedService) { }

  @Input() emp:any;
  EmployeesName:string | undefined;
  Department:string | undefined;
  DateOfJoin:string | undefined;
  DepartmentList: any = [];

  ngOnInit(): void {
    this.service.getAllDepNames().subscribe((data:any) =>{
      this.DepartmentList = data; 
    });
  }

  addEmployee(){
    var val = { 
                EmployeesName: this.EmployeesName,
                Department: this.Department,
                DateOfJoin: this.DateOfJoin,
                PhotoFileName : "empty.pnp"
              };

    this.service.addEmployee(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  editEMployee(){
    var val = { 
                EmployeesId: this.emp.EmployeesId,
                EmployeesName: this.EmployeesName,
                Department: this.Department,
                DateOfJoin: this.DateOfJoin,
                PhotoFileName : "empty.pnp"
              };

    this.service.putEmployee(val).subscribe(res=>{
      alert(res.toString());  
    });
  }
}
