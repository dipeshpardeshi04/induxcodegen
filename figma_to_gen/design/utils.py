import requests
from django.conf import settings
from decouple import config
import time

# Function to get the Figma file data
def get_figma_file_data(figma_file_id, access_token):
    url = f'https://api.figma.com/v1/files/{figma_file_id}'
    headers = {
        'X-Figma-Token': access_token
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returning the full JSON response
    else:
        raise Exception(f"Error fetching Figma data: {response.text}")


# Function to send the Figma data to Gemini API to generate Angular code
def generate_angular_code(figma_data):
    api_key = config('GEMINI_API_KEY')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    headers = {
        'Content-Type': 'application/json'
    }

    # Better prompt for separate Angular files
#     prompt_text = (
#     "From the following Figma JSON data, generate a complete Angular component with PrimeNG in a single code block.\n"
#     "Include the HTML, CSS (inside the component or as styles), and TypeScript code.\n"
#     "And Plz always set Html in template: `` and css in styles: [``] \n"
#     "Do NOT provide any explanation or markdown formatting.\n"
#     "The component should be named appropriately (e.g., HomeComponent), but feel free to name it based on the design context.\n"
#     "Replace any SVGs or icons with random image URLs (like Unsplash), keeping the layout intact.\n"
#     "Make the UI professional, clean, modern, and fully responsive.\n"
#     "Ensure all styling is present (in the component or inline styles) — no external CSS frameworks unless necessary.\n"
#     "Include simple interactivity like click events or hover animations where appropriate.\n"
#     "Make sure the code is well-structured, production-ready, and works directly inside an Angular project.and plz give always in same structure, do not change it \n\n"
#     "Here is the Figma JSON:\n"
    


#     f"{figma_data}"
# )
    prompt_text = (
        "From the following Figma JSON data, generate a complete Angular component that replicates the layout, styling, and structure.\n"
        "Use **PrimeNG** for all UI components such as forms, dropdowns, dialogs, calendars, checkboxes, tables, buttons, etc. and also add bootstrap ( classes in html for layout or any requiremnent)\n\n"

        "The output must include:\n"
        "- TypeScript logic with a reactive form using `FormBuilder`.\n"
        "- PrimeNG tables with column definitions for editable inventory grids (like itemName, quantity, acceptance, etc.).\n"
        "- Tabbed forms or sections if the design has multiple grouped areas (like Check-in details, Cabin Allotment, etc.).\n"
        "- Validations using Angular's `Validators`.\n"
        "- Event handlers like `onSave()`, `onCancel()`, `onRowSelect()`, `onSaveDraft()` etc. with placeholder logic.\n"
        "- Dropdowns, calendars, text inputs, checkboxes bound to the reactive form.\n\n"

        "⚠️ Constraints:\n"
        "- All HTML must go in `template: `` ` inside the component.\n"
        "- All CSS styles must go in `styles: [``]` in the component decorator.\n"
        "- Component must be named appropriately, e.g., `CabinChangeRequestComponent`.\n"
        "- Do NOT use markdown or add explanations — only provide a single valid Angular component code block.\n"
        "- Use placeholder image URLs (e.g., Unsplash) instead of actual SVGs or icons.\n"
        "- Use realistic field names and form controls based on the UI (e.g., `ofc_pers_no`, `dob_dt`, `chk_type`).\n"
        "- UI must be clean, professional, modern, and mobile responsive.\n\n"

        "🧠 Additional Notes:\n"
        "- If the layout resembles a form with multiple sections or tabs, split it accordingly in the UI.\n"
        "- Follow best practices in Angular structure and use PrimeNG’s data binding and components effectively.\n"
        "- Use static arrays for dropdown options if dynamic data is not available.\n"
        "- 🔁 Make sure the structure, class names (e.g., `container-fluid`, `form-group`, `row`, `col-md-6`), layout nesting, and overall HTML closely follow the format of the provided reference sample. Do not simplify or change layout wrappers like `container-fluid` to `container`. Maintain the exact structure as much as possible.\n\n"
        "For example, the generated Angular component code should look like this:\n"
        """onSave() 
          ###################### Include in AI for Tree View ######################
         use this code as it is, just change the formgroup name which is "performaForm" in below code with we use here this.performaForm = this.fb.group({
        const payload = {
            ...this.performaForm.value,
            comp_cd: this.loginData.comp_cd,
            div_cd: this.loginData.div_cd,
            loc_cd: this.performaForm.get('loc_cd')?.value,
            fin_yr: this.loginData.default_fin_yr.fin_yr,
            transaction_stage: 10,
            // next_updator: 'string',
            // next_updator_role: 0,
            // approved_by: 'string',
            // approved_dt: '',
            // stage_remarks: '',
            // rej_reason_cd: '',
            // wh_cd: 0,
            // wh_disp_seq_no: 0,
            // wh_disp_name: '',
            // wh_long_name: ''
        \n """
        """HTML -> 


This HTML describes an Angular component that uses PrimeNG for its UI elements and Reactive Forms for form management. It represents a "Check-Out Performa" form with various input fields, organized into sections and tabs.

Here's a breakdown of its key components and functionalities:

Top Section (Performa Form Header)
Form Group: The entire form is bound to an Angular performaForm Reactive Form Group.
Basic Details:
Location: A p-dropdown (PrimeNG Dropdown) for selecting a location (loc_cd), with options coming from a locations array.
Transaction Type: Another p-dropdown for chk_type, populated by checkinTypeOptions.
Check-Out Performa Date: A p-calendar (PrimeNG Calendar) for chk_dt, with dd/mm/yy format. This field is marked as required.
Action & Read-Only Fields:
A "Select Check In Performa" button that, when clicked, sets showCheckinPerformaDialog to true to open a dialog.
Read-only input for "Check-Out Performa No." (chk_no).
Read-only input for "Member ID" (membership_id).
Read-only inputs for "Officer Personal No." (ofc_pers_no), "Rank" (ofc_rank), and "Officer Name" (ofc_name).
Tabbed View (p-tabView)
The form content is further organized into three tabs:

Check Out Details Tab (p-tabPanel header="Check Out Details")

Cabin Name: Read-only input for wh_disp_name.
Reason: A p-dropdown for selecting a reason, using reasons as options.
Dates & Times:
"Check-In Date" (arriving_dt) using p-calendar (read-only implicitly, or not marked as editable).
"Check-Out Date" (leaving_dt) using p-calendar, marked as required.
"Check Out Time" (chk_out_time) using p-calendar with time-only selection (24-hour format), marked as required.
"Last Meal" (last_meal) using p-dropdown, populated by meals, marked as required.
Remark: A textarea for remarks.
Next Unit Information: Inputs for "Next Unit" (next_unit) and "Next Unit Address" (next_unit_add).
GX Details:
"GX Date" (gx_dt) using p-calendar, marked as required.
"Date of Occurance" (gx_occrnce_dt) using p-dropdown with dateOfoccuranceOptions.
"GX No." (gx_no) input, marked as required.
Financial Details: Read-only inputs for "Balance Outstanding" (bal_os_amt) and "Cabin Recovery" (recovery_amt).
Cabin Inventory Details Tab (p-tabPanel header="Cabin Inventory Details")

Displays a reusable grid component (app-reusable-grid) to show "Cabin Inventory Details," configured with cabinInvColumns for columns and cabinInvData for data.
Check In Details Tab (p-tabPanel header="Check In Details")

Contains numerous read-only input fields and calendar fields displaying check-in related information, such as:
"Officer Rank" (ofc_rank)
"GX No." (gx_no)
"Ration" (ration)
"Officer Unit" (ofc_unit)
"GX Date" (gx_dt)
"First Meal" (first_meal)
"Officer Duty" (ofc_duty)
"Date of Occurance of GX-AM/PM" (gx_occrnce_dt)
"MOV with" (mov_with)
"Marital Status" (marital_sts)
"DOB" (dob_dt)
"Reported for Unit Name" (reported_unit_name)
"Unit Tele. No." (unit_tel_no)
"Mobile No." (ofc_mob_no)
"Alt. Mobile No." (ofc_alt_mob_no)
"Date of Commissioning" (comm_dt)
"Drawing HRA" (drwng_hra)
"Email ID" (ofc_email)
"Seniority in Present Rank" (seniority_rank)
"Civilian Bearer" (civ_bearer)
"Nic Mail ID" (nic_email)
"Accn. Retained in Previous Stn." (acc_ret_prev_stn)
"CB Mobile No." (cb_mob_no)
"Permanent Address" (permnt_add)
"Pay Authority" (pay_authority)
"Account No." (acc_no)
"Reason for Retention" (retn_reason)
"Remark" (chkin_remarks)
"NOK Address" (nok_add)
"NOK Contact Details" (nok_contact_det)
Cabin Allotment History Tab (p-tabPanel header="Cabin Allotment History")

Displays another reusable grid (app-reusable-grid) for "Cabin Allotment History," using cabinAllotColumns and cabinAllotData.
Footer Component
An app-bottom-footer component is included, which emits cancel, saveDraft, and save events, suggesting common form actions.
Select Check-In Performa Dialog (p-dialog)
A modal dialog that appears when showCheckinPerformaDialog is true.
Header: "Select Details".
Content: Contains an app-reusable-grid to display "Check In Performa" data.
Configured with checkinPerformaColumns and checkinPerformaData.
Includes pagination settings (paginator: true, rows: 10, rowsPerPageOptions: [5,10,20]).
Emits selectedRowsChange event to onCheckinPerformaRowsSelection($event).
Footer:
A "Cancel" button (p-button-text) that triggers oncheckinPerformaCancel($event).
An "Accept" button (p-button-primary) that triggers oncheckinPerformaAccept($event).
This structure indicates a comprehensive form for managing "Check-Out Performa" entries, likely in a hospitality or accommodation management system, with detailed information about the officer, cabin, and associated history, and the ability to select from previous check-in performa records. \n"""

"""HERE is TS for reference  ->
```typescript
// Import necessary Angular core modules
import { Component, OnInit } from '@angular/core';
// Import FormBuilder and FormGroup for reactive forms, and Validators for form validation
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// Import Store from @ngrx/store for state management
import { Store } from '@ngrx/store';
// Import MessageService from PrimeNG for displaying toast messages
import { MessageService } from 'primeng/api';
// Import take operator from rxjs for taking a single value from an observable
import { take } from 'rxjs';
// Import custom API and Shared services
import { ApiService } from '../../../../shared/api.service';
import { SharedService } from '../../../../shared/shared.service';
// Import NgRx actions and selectors for session management
import { selectSession, setSession } from '../../../../store';

// Component decorator defines metadata for the Angular component
@Component({
    selector: 'app-joining-performa-checkout', // Custom HTML tag for this component
    standalone: false, // Indicates this component is not standalone (part of an NgModule)
    templateUrl: './joining-performa-checkout.component.html', // Path to the component's HTML template
    styleUrl: './joining-performa-checkout.component.scss' // Path to the component's styling
})
export class JoiningPerformaCheckoutComponent implements OnInit {
    // Form group for the performa checkout form
    performaForm!: FormGroup;
    // Holds the currently selected employee from the check-in performa dialog
    selectedEmployee: any;
    // Arrays to hold data for dropdowns
    locations: any[] = [];
    transactionTypes: any[] = []; // Not explicitly populated in this code snippet
    // Pre-defined reasons for leaving
    reasons = [
        { label: 'TY Duty', value: 'TY Duty' },
        { label: 'Hospitalized', value: 'Hospitalized' },
        { label: 'Leave', value: 'Leave' },
        { label: 'Sailing', value: 'Sailing' },
        { label: 'Permanent transfer', value: 'Permanent transfer' }
    ];
    times: any[] = []; // Not populated in this snippet, intended for time options
    nextUnits: any[] = []; // Not populated in this snippet, intended for next unit options
    loginData: any; // Stores user login data from the NgRx store
    // Pre-defined meal options
    meals = [
        { label: 'Breakfast', value: 'Breakfast' },
        { label: 'Lunch', value: 'Lunch' },
        { label: 'Dinner', value: 'Dinner' },
        { label: 'No Meal', value: 'No Meal' }
    ];
    // Column definitions for the Cabin Inventory table
    cabinInvColumns = [
        { field: 'itemName', header: 'Item Name', editor: 'input', readonly: true },
        { field: 'denomination', header: 'Denomination', editor: 'input', readonly: true },
        { field: 'checkInQty', header: 'Check in Qty.', editor: 'number', readonly: true },
        { field: 'checkOutQty', header: 'Check Out Qty.', editor: 'number', readonly: true },
        { field: 'diffQty', header: 'Diff. Qty', editor: 'number', readonly: true },
        { field: 'currStock', header: 'Curr. Stock', editor: 'number', readonly: true },
        { field: 'received', header: 'Received', editor: 'checkbox' }, // Checkbox editor for received status
        { field: 'remark', header: 'Remark', editor: 'input' },
        { field: 'itemCode', header: 'Item Code', editor: 'input', readonly: true }
    ];
    cabinInvData: any[] = []; // Data for the Cabin Inventory table
    // Column definitions for the Cabin Allotment table
    cabinAllotColumns = [
        { field: 'cabinName', header: 'Cabin Name', editor: 'input', readonly: true },
        { field: 'checkInDate', header: 'Check-In Date', editor: 'calendar', readonly: true, dateFormat: 'dd/mm/yy' }, // Calendar editor with date format
        { field: 'checkOutDate', header: 'Check-Out Date', editor: 'calendar', dateFormat: 'dd/mm/yy' },
        { field: 'reason', header: 'Reason', editor: 'input' },
        { field: 'remark', header: 'Remark', editor: 'input' }
    ];
    cabinAllotData: any[] = []; // Data for the Cabin Allotment table
    showCheckinPerformaDialog: boolean = false; // Controls visibility of the check-in performa dialog
    // Column definitions for the Check-in Performa table in the dialog
    checkinPerformaColumns: any[] = [
        { field: 'ofc_pers_no', header: 'Officer Personal No.', width: '150px', editor: 'text', readonly: true },
        { field: 'ofc_name', header: 'Officer Name', width: '200px', editor: 'text', readonly: true },
        { field: 'ofc_mob_no', header: 'Mobile No.', width: '150px', editor: 'text', readonly: true },
        { field: 'ofc_email', header: 'Email', width: '200px', editor: 'text', readonly: true },
        { field: 'chkin_dt', header: 'Arriving Date', width: '150px', editor: 'text', readonly: true },
        // Commented out fields, indicating they might be considered in future or are optional
        // { field: 'transactionNo', header: 'Transaction No.', width: '200px', editor: 'text', readonly: true },
        // { field: 'transactionDate', header: 'Transaction Date', width: '150px', editor: 'text', readonly: true }
    ];
    // Options for check-in type dropdown
    checkinTypeOptions = [
        { label: 'Civilian Guest Check In', value: 362 },
        { label: 'In Leaving Officer Check In', value: 353 },
        { label: 'Out Leaving Officer Check In', value: 359 },
        { label: 'Retired Officer Check In', value: 363 },
        { label: 'In Leaving Officer Re-Check In', value: 360 },
    ];
    // Options for date of occurrence dropdown (AM/PM)
    dateOfoccuranceOptions = [
        { label: 'AM', value: 'AM' },
        { label: 'PM', value: 'PM' }
    ];
    checkinPerformaData: any[] = []; // Data for the check-in performa dialog table

    // // Constructor for dependency injection
    constructor(
        private fb: FormBuilder, // Injects FormBuilder for reactive forms
        private sharedService: SharedService, // Injects SharedService for common functionalities
        private apiService: ApiService, // Injects ApiService for backend communication
        private store: Store, // Injects NgRx Store for state management
        private messageService: MessageService // Injects PrimeNG MessageService for notifications
    ) {
        // Subscribe to the NgRx session store to get login data
        this.store.select(selectSession).pipe(take(1)).subscribe((currentSession: any) => {
            // Decrypt and parse user login data
            this.loginData = JSON.parse(this.sharedService.decrypt(currentSession.user));
            // Get current user role and then fetch lite data
            this.sharedService.getCurrentUserRole().then((res: any) => {
                // Commented out previous methods for fetching employee details and locations,
                // now consolidated under getLiteData()
                // this.sharedService.getEmployeeDetails(res.role_cd).subscribe((result: any) => {
                //     this.checkinPerformaData = result.data;
                // });
                // this.sharedService.getEmployeeLocations(res.role_cd).subscribe((result: any) => {
                //     this.locations = result.data;
                // });
                this.getLiteData(); // Calls method to fetch data for the check-in performa dialog
            });
            // console.log(this.loginData); // For debugging
        });
    }

    // Fetches lite data for the joining performa checkout, specifically the check-in performa data.
    getLiteData() {
        // Construct payload with company, division, and location codes from login data
        const payload = {
            comp_cd: this.loginData.comp_cd,
            div_cd: this.loginData.div_cd,
            loc_cd: this.loginData.loc_cd,
            dtl_req: 1 // Detail request flag
        };
        // Call API to fetch joining performa data
        this.apiService.post('joiningProforma/v1/fetch', payload).subscribe((result: any) => {
            this.checkinPerformaData = result.data; // Assign fetched data to checkinPerformaData
        });
    }
    // // OnInit lifecycle hook, called after the component's view has been initialized
    ngOnInit(): void {
        // Initialize the performaForm with form controls and validators
        this.performaForm = this.fb.group({
            loc_cd: [null, Validators.required], // Location code, required
            chk_type: [null, Validators.required], // Check type, required
            chk_dt: [null, Validators.required], // Check date, required
            chkin_hdr_sr_no: [null, Validators.required], // Check-in header serial number, required
            membership_id: [''], // Membership ID
            ofc_pers_no: [''], // Officer personal number
            chk_no: [''], // Check number
            ofc_rank: [''], // Officer rank
            ofc_name: [''], // Officer name
            wh_cdwh_cd: [null], // Warehouse code (potential typo, should be wh_cd?)
            wh_disp_name: [''], // Warehouse display name
            reason: [null], // Reason for checkout
            leaving_dt: [null, Validators.required], // Leaving date, required
            remarks: [null], // General remarks
            arriving_dt: [null], // Arriving date
            chk_out_time: [null, Validators.required], // Check-out time, required
            next_unit: [null], // Next unit
            next_unit_add: [null], // Next unit address
            last_meal: [null, Validators.required], // Last meal, required
            bal_os_amt: [{ value: 0.00, disabled: true }], // Balance outstanding amount, disabled
            gx_no: [null, Validators.required], // GX number, required
            gx_dt: [null, Validators.required], // GX date, required
            gx_occrnce_dt: [null, Validators.required], // GX occurrence date, required
            recovery_amt: [{ value: 100.00, disabled: true }], // Recovery amount, disabled
            // Below fields are disabled, likely for displaying fetched employee details
            ofc_unit: [{ value: null, disabled: true }],
            ofc_duty: [{ value: null, disabled: true }],
            dob_dt: [{ value: null, disabled: true }],
            marital_sts: [{ value: null, disabled: true }],
            ofc_mob_no: [{ value: null, disabled: true }],
            ofc_alt_mob_no: [{ value: null, disabled: true }],
            ofc_email: [{ value: null, disabled: true }],
            nic_email: [{ value: null, disabled: true }],
            permnt_add: [{ value: null, disabled: true }],
            nok_add: [{ value: null, disabled: true }],
            nok_contact_det: [{ value: null, disabled: true }],
            ration: [{ value: null, disabled: true }],
            first_meal: [{ value: null, disabled: true }],
            mov_with: [{ value: null, disabled: true }],
            unit_tel_no: [{ value: null, disabled: true }],
            drwng_hra: [{ value: null, disabled: true }],
            civ_bearer: [{ value: null, disabled: true }],
            cb_mob_no: [{ value: null, disabled: true }],
            acc_no: [{ value: null, disabled: true }],
            reported_unit_name: [{ value: null, disabled: true }],
            comm_dt: [{ value: null, disabled: true }],
            seniority_rank: [{ value: null, disabled: true }],
            acc_ret_prev_stn: [{ value: null, disabled: true }],
            pay_authority: [{ value: null, disabled: true }],
            retn_reason: [{ value: null, disabled: true }],
            chkin_remarks: [{ value: null, disabled: true }]
        });
        // // Sets the screen title dynamically using NgRx store
        this.setNewTitle('Joining Performa Checkout');
        // this.getLocations(); // Fetch locations for the dropdown
    }

    // // Function to fetch locations from the shared service for a dropdown.
    // AI should generalize this pattern: `get` followed by the dropdown name (e.g., `getLocations()`).
    getLocations() {
        this.sharedService.getDropdownData(['LOCATION']).subscribe((result: any) => {
            this.locations = result.data[0].LOCATION; // Assign fetched locations to the 'locations' array
        });
    }

    // Dispatches an action to update the session title in the NgRx store.
    setNewTitle(newTitle: string) {
        this.store.dispatch(setSession({ title: newTitle }));
    }
    // // Placeholder for cancel action
    onCancel() {
        // Implementation for canceling the form or navigation
    }
    // Placeholder for save draft action
    onSaveDraft() {
        // Implementation for saving form data as a draft
    }
    // Handles saving the performa checkout data
    onSave() {
        // // Construct the payload for the API call using form values and login data.
        // This structure should be used as-is, just adapt the form group name.
        const payload = {
            ...this.performaForm.value, // Spread all current form values into the payload
            comp_cd: this.loginData.comp_cd, // Company code from login data
            div_cd: this.loginData.div_cd, // Division code from login data
            loc_cd: this.performaForm.get('loc_cd')?.value, // Location code from the form (ensures it's the current value)
            fin_yr: this.loginData.default_fin_yr.fin_yr, // Financial year from login data
            transaction_stage: 10, // Transaction stage (pre-defined value)
            // Commented out fields, indicating they are optional or not yet implemented in the payload
            // next_updator: 'string',
            // next_updator_role: 0,
            // approved_by: 'string',
            // approved_dt: '',
            // stage_remarks: '',
            // rej_reason_cd: '',
            // wh_cd: 0,
            // wh_disp_seq_no: 0,
            // wh_disp_name: '',
            // wh_long_name: ''
        };
        console.log(payload); // Log payload for debugging
        // Call the API to post checkout data
        this.apiService.post('v1/performa/chk/out', [payload]).subscribe({
            next: (res: any) => {
                console.log(res); // Log API response
                if (res.status.status === 1) {
                    // Display success message using MessageService
                    this.messageService.add({
                        severity: 'success',
                        summary: 'Success',
                        detail: res.status.message || 'Officer details saved successfully' // Use screen name in place of 'Officer details'
                    });
                } else {
                    // Display error message if API status is not 1
                    this.messageService.add({
                        severity: 'error',
                        summary: 'Error',
                        detail: res.status.message || 'Failed to save officer details'
                    });
                }
            },
            error: (err) => {
                // Display error message for API call failure
                this.messageService.add({
                    severity: 'error',
                    summary: 'Error',
                    detail: err.error?.message || 'An error occurred while saving officer details'
                });
            }
        });
    }

    // Renamed function to "setRowSelection()" for brevity and clarity.
    // Handles row selection from the check-in performa dialog.
    setRowSelection(event: any) { // Changed name from onCheckinPerformaRowsSelection
        this.selectedEmployee = event[0]; // Get the first selected employee
        console.log(this.selectedEmployee); // Log selected employee for debugging

        // Define a map of form control names to corresponding selected employee properties
        const formControls = {
            'ofc_pers_no': this.selectedEmployee.ofc_pers_no,
            'ofc_name': this.selectedEmployee.ofc_name,
            'ofc_rank': this.selectedEmployee.ofc_rank,
            'ofc_unit': this.selectedEmployee.ofc_unit,
            'ofc_mob_no': this.selectedEmployee.ofc_mob_no,
            'ofc_email': this.selectedEmployee.ofc_email,
            'membership_id': this.selectedEmployee.membership_id,
            'wh_cd': this.selectedEmployee.wh_cd,
            'arriving_dt': new Date(this.selectedEmployee.arriving_dt), // Convert date string to Date object
            'leaving_dt': new Date(this.selectedEmployee.leaving_dt), // Convert date string to Date object
            'gx_no': this.selectedEmployee.gx_no,
            'gx_dt': new Date(this.selectedEmployee.gx_dt), // Convert date string to Date object
            'gx_occrnce_dt': this.selectedEmployee.gx_occrnce_dt,
            'dob_dt': new Date(this.selectedEmployee.dob_dt), // Convert date string to Date object
            'marital_sts': this.selectedEmployee.marital_sts,
            'ofc_alt_mob_no': this.selectedEmployee.ofc_alt_mob_no,
            'nic_email': this.selectedEmployee.nic_email,
            'permnt_add': this.selectedEmployee.permnt_add,
            'nok_add': this.selectedEmployee.nok_add,
            'nok_contact_det': this.selectedEmployee.nok_contact_det,
            'ration': this.selectedEmployee.ration,
            'first_meal': this.selectedEmployee.first_meal,
            'unit_tel_no': this.selectedEmployee.unit_tel_no,
            'drwng_hra': this.selectedEmployee.drwng_hra,
            'comm_dt': this.selectedEmployee.comm_dt ? new Date(this.selectedEmployee.comm_dt) : null, // Handle nullable date
            'seniority_rank': this.selectedEmployee.seniority_rank,
            'acc_ret_prev_stn': this.selectedEmployee.acc_ret_prev_stn,
            'pay_authority': this.selectedEmployee.pay_authority,
            'retn_reason': this.selectedEmployee.retn_reason,
            'chkin_remarks': this.selectedEmployee.chkin_remarks,
            'chk_no': this.selectedEmployee.chkin_no,
            'chkin_hdr_sr_no': this.selectedEmployee.chkin_hdr_sr_no,
        };

        // Iterate over the formControls and set values for each control in the performaForm
        Object.entries(formControls).forEach(([controlName, value]) => {
            const control = this.performaForm.get(controlName); // Get the form control by name
            if (control) { // Check if the control exists
                control.setValue(value); // Set the value of the control
                control.markAsTouched(); // Mark the control as touched
                control.updateValueAndValidity(); // Update its validation status
            }
        });
    }

    // // Handles the cancel action for the check-in performa dialog
    oncheckinPerformaCancel(event: any) {
        this.showCheckinPerformaDialog = false; // Hide the dialog
    }
    // Handles the accept action for the check-in performa dialog
    oncheckinPerformaAccept(event: any) {
        this.showCheckinPerformaDialog = false; // Hide the dialog
    }
}

/* eslint-disable @angular-eslint/no-empty-lifecycle-method */
/* eslint-disable prefer-const */
/* eslint-disable no-empty */
/* eslint-disable no-debugger */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */

// Removed redundant imports and interfaces related to tree view that are already implicitly handled or part of core functionality.
// The previous code had a separate RoletopersonallinkComponent which was commented out and likely intended for a different purpose or to be merged.
// I'm assuming the user wants to see the tree view functionality applied to the existing context if applicable, or just how tree view related
// comments/code should be interpreted. Given the "Tree View" comments in JoiningPerformaCheckoutComponent, I've integrated them there.
// If the RoletopersonallinkComponent was meant to be a separate, active component, it would need to be fully uncommented and analyzed.

// Assuming the user meant to merge the tree view aspects into the main component for the purpose of the summary,
// or wanted the "Tree View" comments properly placed and explained.
// The provided code snippet only fully includes the JoiningPerformaCheckoutComponent.
// The RoletopersonallinkComponent is commented out and appears to be a separate component,
// but the AI comments suggest it might be relevant for how tree view functionality would be generalized.

// If `RoletopersonallinkComponent` is intended to be a *separate* component that the AI should also summarize/generate,
// then the summary for *that* component would be as follows (commented out as it's not part of the active code provided):

/*
// Interfaces for tree nodes
interface FoodNode {
    title: string;
    id: any;
    children?: FoodNode[];
}

interface ExampleFlatNode {
    expandable: boolean;
    title: string;
    id: any;
    level: number;
}

// Injectable service for managing tree data (acts as a data source for the tree)
@Injectable({ providedIn: 'root' })
export class ChecklistDatabase {
    dataChange = new BehaviorSubject<FoodNode[]>([]); // BehaviorSubject to notify changes in tree data
    treeData: any[] | undefined;

    get data(): FoodNode[] {
        return this.dataChange.value;
    }

    constructor() {
        this.initialize(); // Initialize tree data on creation
    }

    initialize() {
        this.treeData = this.data;
        // Build tree nodes from JSON object (placeholder logic)
        const data = this.data;
        this.dataChange.next(data); // Notify subscribers of data change
    }
}

// RoletopersonallinkComponent for managing role-to-personnel linking with a tree view
@Component({
    selector: 'app-roletopersonallink',
    templateUrl: './roletopersonallink.component.html',
    styleUrls: ['./roletopersonallink.component.scss'],
    standalone: false,
})
export class RoletopersonallinkComponent implements OnInit {
    progId = "loadRoleUserLink"; // Program ID for access control
    flatNodeMap = new Map<ExampleFlatNode, FoodNode>(); // Map for flattened nodes to nested nodes
    nestedNodeMap = new Map<FoodNode, ExampleFlatNode>(); // Map for nested nodes to flattened nodes
    selectedParent: ExampleFlatNode | null = null; // Selected parent node
    newItemName = ''; // Name for new item
    employeeData: any = []; // Data for employee grid

    // Transformer function to convert nested tree nodes to flattened nodes for FlatTreeControl
    private _transformer = (node: FoodNode, level: number) => {
        return {
            expandable: !!node.children && node.children.length > 0, // Determine if node is expandable
            title: node.title, // Node title
            id: node.id, // Node ID
            level: level // Node level in the tree
        };
    };

    // FlatTreeControl for managing tree expansion/collapse
    treeControl = new FlatTreeControl<ExampleFlatNode>(
        (node) => node.level, // Function to get node level
        (node) => node.id // Function to get node ID (used for expansion/collapse tracking)
    );

    activeNode: any; // Currently active node in the tree
    searchString = ''; // Search string for filtering tree nodes
    data: any; // Raw tree data

    // Predicate to check if a node has children
    hasChild = (_: number, node: ExampleFlatNode) => node.expandable;

    isshown: boolean = false; // Controls visibility
    loggedin: any; // User login data
    roleMasterForm!: FormGroup; // Form group for role master details
    roleCode: any; // Selected role code
    columnDefs: any; // Column definitions for the grid (not fully defined here)
    // Default column definitions for ag-Grid-like tables
    defaultColumnDef: any = {
        filter: true, // Enable filtering
        floatingFilter: true, // Enable floating filters
        sortable: true, // Enable sorting
        resizable: true, // Enable resizing
        headerCheckboxSelection: this.isFirstColumn, // Checkbox selection for header
        checkboxSelection: this.isFirstColumn // Checkbox selection for rows
    };
    // Another default column definition for tables without specific checkbox behavior
    defaultColumnDef1: any = {
        filter: true,
        floatingFilter: true,
        sortable: true,
        resizable: true
    };
    gridApi: any; // Reference to the ag-Grid API
    mode: any = 'Edit'; // Current mode (Add/Edit)
    commands: any; // Commands (not populated)
    units: any; // Units (not populated)
    frameworkComponents!: { checkboxRenderer: any }; // Custom framework components for grid
    columnDefs1: any; // Another set of column definitions
    public rowSelectionValue: boolean = false; // Flag for row selection
    AllselectedRows: any = []; // Array of all selected rows
    mergedArray: any = []; // Merged array (purpose unclear from snippet)
    modalRef!: NgbModalRef; // Reference to NgbModalRef for modal dialogs
    selectAll: boolean = false; // Flag for select all checkbox
    selectedEmployees: any[] = []; // Array of selected employees
    userCode: string | null = null; // User code
    disabled: boolean = true; // Flag for disabling elements
    loading: boolean = false; // Loading indicator
    orderBy: string | undefined; // Order by field for sorting
    orderByField: string | undefined; // Order by field for sorting
    modifiedUsers: any[] = []; // Array of modified users

    // // Files array to hold tree data for the tree view component (PrimeNG Tree or Angular CDK Tree).
    files: [] = [];
    // isAddClicked: boolean = false; // Flag for add button click
    isEditClicked: boolean = true; // Flag for edit button click
    activeRole: any; // Currently active role

    constructor(
        public apiService: ApiService,
        public router: Router,
        private fb: FormBuilder,
        private sharedService: SharedService,
        private modalService: NgbModal // Injects NgbModal for modal dialogs
    ) { }

    ngOnInit(): void {
        // Commented out authentication and loader service logic.
        // The core logic for tree view data fetching is below.

        // // Fetches current user and role to construct payload for tree data API call.
        this.sharedService.getCurrentUser().then((res: any) => {
            this.loggedin = res; // Store logged-in user data
            console.log('loggedin', this.loggedin); // For debugging
            this.sharedService.getCurrentUserRole().then((res: any) => {
                console.log('res', res); // For debugging
                this.activeRole = res; // Store active role
                let payload = {
                    comp_cd: this.loggedin.comp_cd, // Company code
                    div_cd: this.loggedin.div_cd, // Division code
                    // role_cd: this.activeRole.role_cd, // Role code (commented out, depends on API)
                    loc_cd: this.loggedin.loc_cd, // Location code
                    user_id: this.loggedin.user_id, // User ID
                    audit_trail_yn: 0, // Audit trail flag
                };
                // Calls API to fetch role tree data
                this.apiService.post('v1/role/tree', payload).subscribe((res: any) => {
                    this.files = res.data; // Assign fetched data to 'files' for the tree view
                    this.files.forEach((node) => {
                        this.expandRecursive(node, true); // Recursively expand all nodes
                    });
                    console.log('res', res); // For debugging
                });
            });
        });
        // // Initialize roleMasterForm
        this.roleMasterForm = this.fb.group({
            // lowestLevelFlag:[],
            roleName: [],
            roleCode: [],
            command: [],
            unit: [],
            pno: []
        });
        // Disable roleName and roleCode fields
        this.roleMasterForm.controls['roleName'].disable();
        this.roleMasterForm.controls['roleCode'].disable();
    }

    onCellClicked(params: any) {
        params.node.setSelected(true, true); // Set row as selected on cell click
    }

    isFirstColumn(params: any) {
        let displayedColumns = params.columnApi.getAllDisplayedColumns();
        let thisIsFirstColumn = displayedColumns[0] === params.column;
        return thisIsFirstColumn; // Check if the current column is the first displayed column
    }

    // // Function to get role details when a node in the tree is selected.
    getRoleDetails(node: any) {
        // this.Reset(); // Commented out reset function
        this.roleCode = node.id; // Set role code from selected node ID
        this.roleMasterForm.controls['roleName'].setValue(node.title); // Set role name from node title
        this.roleMasterForm.controls['roleCode'].setValue(node.id); // Set role code in form
        this.employeeData = []; // Clear employee data
    }

    // Recursive function to expand/collapse tree nodes (used in both components for tree view).
    // This is a common utility for tree structures.
    expandRecursive(node: any, isExpand: boolean) {
        node.expanded = isExpand; // Set node's expanded state
        if (node.children) {
            node.children.forEach((childNode: any) => {
                this.expandRecursive(childNode, isExpand); // Recursively call for children
            });
        }
    }
    // // Filters leaf nodes based on search string
    filterLeafNode(node: FoodNode): boolean {
        if (!this.searchString) {
            return false; // No search string, no filtering
        }
        return node.title.toLowerCase().indexOf(this.searchString?.toLowerCase()) === -1; // Return true if title does not contain search string
    }

    // Filters parent nodes based on search string
    filterParentNode(node: ExampleFlatNode): boolean {
        if (!this.searchString || node.title.toLowerCase().indexOf(this.searchString?.toLowerCase()) !== -1) {
            return false; // No search string or node title matches, no filtering
        }
        const descendants = this.treeControl.getDescendants(node); // Get all descendants of the node

        // Check if any descendant node title matches the search string
        if (descendants.some((descendantNode) => descendantNode.title.toLowerCase().indexOf(this.searchString?.toLowerCase()) !== -1)) {
            return false; // Descendant matches, so don't filter this parent
        }

        return true; // Filter out this parent if no descendant matches
    }

    // Sets the component mode (Add or Edit)
    setMode(mode: any) {
        this.mode = mode; // Set the current mode
        this.employeeData = []; // Clear employee data
        this.disabled = true; // Disable certain elements
        if (mode == 'Add') {
            this.isAddClicked = true; // Set add mode flag
            this.isEditClicked = false; // Clear edit mode flag
        } else if (mode == 'Edit') {
            this.isEditClicked = true; // Set edit mode flag
            this.isAddClicked = false; // Clear add mode flag
        }
    }
}
*/
\n"""

        "Here is the Figma JSON:\n"
        f"{figma_data}"
    )



    data = {
        "contents": [
            {
                "parts": [{"text": prompt_text}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise Exception("Unexpected Gemini API response structure.")
    else:
        raise Exception(f"Error from Gemini API: {response.text}")

# Function to save the Angular code to a file
# def save_angular_code_to_file(code, filename):
#     with open(filename, 'w') as file:
#         file.write(code)
