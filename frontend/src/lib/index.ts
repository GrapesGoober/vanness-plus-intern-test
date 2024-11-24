// place files you want to import through the `$lib` alias in this folder.

export enum InternStatus {
    NEW  = "New",
    WIP  = "WIP",
    WAIT = "Wait",
    PASS = "Pass",
    FAIL = "Fail",
    HIRE = "Hire",
}

export type InternInfo = {
    name: string;
    applied_date: string; // format yyyy-mm-dd
    role: string;
    status: InternStatus;
}

export type InternInfoWithId = InternInfo & {
    id: number;
}

export type InternFilter = {
    name_contains:  string;
    applied_after:  string;  // format yyyy-mm-dd
    applied_before: string;  // format yyyy-mm-dd
    status:         InternStatus;
}

export function GetDefaultInternFilter(): InternFilter {
    let appliedBeforeDefault: string = "2020-01-01";
    let dateNow: string = 
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0];

    let filter: InternFilter = {
        name_contains: "",
        applied_after: appliedBeforeDefault,
        applied_before: dateNow, 
        status: InternStatus.HIRE
    };

    return filter;
}

export namespace API {
    export async function GetInterns (filter: InternFilter): Promise<Array<InternInfoWithId>> {
        // Fetch the list of interns
        const queryString = new URLSearchParams(filter).toString();

        // TODO: proper error handling of fetch returns
        const response = await fetch('/api/intern?' + queryString, {
            method: 'GET', // Specify GET method for retrieving data
            headers: {
            'Content-Type': 'application/json', // Optional header for JSON data
            },
        });
        // Cast them to InternInfoWithId
        return <Array<InternInfoWithId>> (await response.json());
    }

    export async function AddIntern(intern: InternInfo): Promise<boolean> {

        const response = await fetch('/api/intern', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(intern)
        });

        return response.ok;
    }
}